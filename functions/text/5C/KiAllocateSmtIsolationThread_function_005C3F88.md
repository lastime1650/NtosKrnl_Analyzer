# KiAllocateSmtIsolationThread

- RVA: `0x005C3F88`–`0x005C3FE4` (길이 `92` bytes)
- VA: `0x00000001405C3F88`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000718C0`
- 디코드: `26`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x005C3FBB` → [KiAllocatePrcbThread](../5B/KiAllocatePrcbThread_function_005B9130.md) (function, `0x005B9130`)
- `0x005C3FCC` → [PsAssignThreadId](../47/PsAssignThreadId_function_004745F0.md) (function, `0x004745F0`)

### Direct callers
- [KiAllocatePrcbThreads](../5B/KiAllocatePrcbThreads_function_005B6C2C.md) at `0x005B6C69`
- [KiCompleteBootProcessorContextInitialization](../5B/KiCompleteBootProcessorContextInitialization_function_005B7634.md) at `0x005B7725`

### Static image references
- `0x005C3F99` → RVA `0x00E07120` (`.data`; read)
- `0x005C3FB4` → RVA `0x005C4070` (`KiExecuteSmtIsolationThread`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005C3F88  4C 8B DC                        mov r11, rsp
005C3F8B  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
005C3F8F  57                              push rdi
005C3F90  48 83 EC 40                     sub rsp, 0x40
005C3F94  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
005C3F99  48 8D 05 80 31 84 00            lea rax, [rip + 0x843180]
005C3FA0  49 83 63 18 00                  and qword ptr [r11 + 0x18], 0
005C3FA5  48 8B F9                        mov rdi, rcx
005C3FA8  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
005C3FAC  49 8D 4B 18                     lea rcx, [r11 + 0x18]
005C3FB0  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
005C3FB4  48 8D 15 B5 00 00 00            lea rdx, [rip + 0xb5]
005C3FBB  E8 70 51 FF FF                  call 0x1405b9130
005C3FC0  85 C0                           test eax, eax
005C3FC2  78 14                           js 0x1405c3fd8
005C3FC4  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
005C3FC9  48 8B CB                        mov rcx, rbx
005C3FCC  E8 1F 06 EB FF                  call 0x1404745f0
005C3FD1  85 C0                           test eax, eax
005C3FD3  78 03                           js 0x1405c3fd8
005C3FD5  48 89 1F                        mov qword ptr [rdi], rbx
005C3FD8  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
005C3FDD  48 83 C4 40                     add rsp, 0x40
005C3FE1  5F                              pop rdi
005C3FE2  C3                              ret
005C3FE3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAllocateSmtIsolationThread(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 32) = v_rip + 8663424;
    v_stack_m28 = a2;
    result = KiAllocatePrcbThread(v_rsp + 24, v_rip + 181, a3, a4);
    if (sign_flag) goto loc_005C3FD8;
    result = PsAssignThreadId(v_stack_p18, v_rip + 181, a3, a4);
    if (!(sign_flag)) {
        *(unsigned __int64 *)(a1) = v_stack_p18;
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiAllocateSmtIsolationThread(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint32_t v_stack_m28;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x20) = v_rip + 8663424;
    v_stack_m28 = Arg2;
    result = KiAllocatePrcbThread(local_rsp + 24, v_rip + 181, a3, a4);
    if (sign_flag) goto loc_005C3FD8;
    result = PsAssignThreadId(v_stack_p18, v_rip + 181, a3, a4);
    if (!(sign_flag)) {
        *(uint64_t *)(arg1) = v_stack_p18;
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005C3F88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005C3F88[BB_005C3F88]
  bb_005C3FC4[BB_005C3FC4]
  bb_005C3FD5[BB_005C3FD5]
  bb_005C3FD8[BB_005C3FD8]
  bb_005C3FE3[BB_005C3FE3]
  bb_005C3F88 -->|branch| bb_005C3FD8
  bb_005C3F88 -->|fallthrough| bb_005C3FC4
  bb_005C3FC4 -->|branch| bb_005C3FD8
  bb_005C3FC4 -->|fallthrough| bb_005C3FD5
  bb_005C3FD5 -->|flow| bb_005C3FD8
```
