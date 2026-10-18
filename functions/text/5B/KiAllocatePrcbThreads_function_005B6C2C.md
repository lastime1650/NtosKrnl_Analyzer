# KiAllocatePrcbThreads

- RVA: `0x005B6C2C`–`0x005B6C84` (길이 `88` bytes)
- VA: `0x00000001405B6C2C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `24`개 명령, `88/88` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005B6C55` → [KiAllocateDpcDelegateThread](KiAllocateDpcDelegateThread_function_005B697C.md) (function, `0x005B697C`)
- `0x005B6C69` → [KiAllocateSmtIsolationThread](../5C/KiAllocateSmtIsolationThread_function_005C3F88.md) (function, `0x005C3F88`)

### Direct callers
- [KiStartDynamicProcessor](../../page/74/KiStartDynamicProcessor_function_007456C8.md) at `0x00745983`
- [KeStartAllProcessors](../../init/C3/KeStartAllProcessors_function_00C36F78.md) at `0x00C372DD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B6C2C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005B6C31  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
005B6C36  57                              push rdi
005B6C37  48 83 EC 20                     sub rsp, 0x20
005B6C3B  48 8B 81 C0 00 00 00            mov rax, qword ptr [rcx + 0xc0]
005B6C42  48 8B D9                        mov rbx, rcx
005B6C45  48 81 C1 38 38 00 00            add rcx, 0x3838
005B6C4C  0F B7 B8 8A 00 00 00            movzx edi, word ptr [rax + 0x8a]
005B6C53  8B D7                           mov edx, edi
005B6C55  E8 22 FD FF FF                  call 0x1405b697c
005B6C5A  33 F6                           xor esi, esi
005B6C5C  85 C0                           test eax, eax
005B6C5E  78 13                           js 0x1405b6c73
005B6C60  48 8D 8B 80 8E 00 00            lea rcx, [rbx + 0x8e80]
005B6C67  8B D7                           mov edx, edi
005B6C69  E8 1A D3 00 00                  call 0x1405c3f88
005B6C6E  85 C0                           test eax, eax
005B6C70  0F 49 C6                        cmovns eax, esi
005B6C73  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005B6C78  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
005B6C7D  48 83 C4 20                     add rsp, 0x20
005B6C81  5F                              pop rdi
005B6C82  C3                              ret
005B6C83  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAllocatePrcbThreads(__int64 a1)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (0x3838ULL);
    result = KiAllocateDpcDelegateThread(a1, (unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 192) + 138))), a3, a4);
    v_rsi = 0;
    if (!(sign_flag)) {
        a1 = a1 + 36480;
        a2 = (unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 192) + 138));
        result = KiAllocateSmtIsolationThread(a1, a2, a3, a4);
        if (!sign_flag) { result = 0; }
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiAllocatePrcbThreads(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (0x3838ULL);
    result = KiAllocateDpcDelegateThread(Arg1, (uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x8A))), a3, a4);
    local_rsi = 0;
    if (!(sign_flag)) {
        Arg1 = Arg1 + 36480;
        a2 = (uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0xC0) + 0x8A));
        result = KiAllocateSmtIsolationThread(Arg1, a2, a3, a4);
        if (!sign_flag) { result = 0; }
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC0` | `64` | `R` |
| `Arg1` | `+ 0x8E80` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B6C2C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B6C2C[BB_005B6C2C]
  bb_005B6C60[BB_005B6C60]
  bb_005B6C73[BB_005B6C73]
  bb_005B6C83[BB_005B6C83]
  bb_005B6C2C -->|branch| bb_005B6C73
  bb_005B6C2C -->|fallthrough| bb_005B6C60
  bb_005B6C60 -->|flow| bb_005B6C73
```
