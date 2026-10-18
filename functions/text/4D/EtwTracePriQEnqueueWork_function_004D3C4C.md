# EtwTracePriQEnqueueWork

- RVA: `0x004D3C4C`–`0x004D3CD3` (길이 `135` bytes)
- VA: `0x00000001404D3C4C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00065FB8`
- 디코드: `32`개 명령, `135/135` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004D3CBB` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x004D3CC8` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KeInsertPriQueue](../21/KeInsertPriQueue_function_0021EDD0.md) at `0x0021EF8B`

### Static image references
- `0x004D3C53` → RVA `0x00E0A740` (`.data`; read)
- `0x004D3C62` → RVA `0x00FC6B1C` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004D3C4C  4C 8B DC                        mov r11, rsp
004D3C4F  48 83 EC 68                     sub rsp, 0x68
004D3C53  48 8B 05 E6 6A 93 00            mov rax, qword ptr [rip + 0x936ae6]
004D3C5A  48 33 C4                        xor rax, rsp
004D3C5D  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
004D3C62  8B 05 B4 2E AF 00               mov eax, dword ptr [rip + 0xaf2eb4]
004D3C68  A8 08                           test al, 8
004D3C6A  75 54                           jne 0x1404d3cc0
004D3C6C  8B 81 10 05 00 00               mov eax, dword ptr [rcx + 0x510]
004D3C72  49 8D 4B D8                     lea rcx, [r11 - 0x28]
004D3C76  49 89 53 C8                     mov qword ptr [r11 - 0x38], rdx
004D3C7A  BA 01 00 00 00                  mov edx, 1
004D3C7F  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
004D3C83  49 8D 43 C8                     lea rax, [r11 - 0x38]
004D3C87  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
004D3C8B  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
004D3C90  41 F6 D9                        neg r9b
004D3C93  45 89 43 D4                     mov dword ptr [r11 - 0x2c], r8d
004D3C97  41 B9 4F 05 00 00               mov r9d, 0x54f
004D3C9D  C7 44 24 48 10 00 00 00         mov dword ptr [rsp + 0x48], 0x10
004D3CA5  1B C0                           sbb eax, eax
004D3CA7  41 B8 00 00 00 21               mov r8d, 0x21000000
004D3CAD  25 00 18 00 00                  and eax, 0x1800
004D3CB2  05 02 06 60 00                  add eax, 0x600602
004D3CB7  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
004D3CBB  E8 90 16 D6 FF                  call 0x140235350
004D3CC0  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
004D3CC5  48 33 CC                        xor rcx, rsp
004D3CC8  E8 73 89 1D 00                  call 0x1406ac640
004D3CCD  48 83 C4 68                     add rsp, 0x68
004D3CD1  C3                              ret
004D3CD2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTracePriQEnqueueWork(__int64 a1, __int64 a2, int a3, unsigned __int8 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned int v_stack_m30;
    unsigned int v_stack_m48;

    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 9661158)) ^ (v_rsp);
    v_stack_m18 = result;
    result = (unsigned int)(*(unsigned int *)(v_rip + 11480756));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11480756)))) & (8)) == 0) {
        result = *(unsigned int *)(a1 + 1296);
        a1 = v_rsp - 40;
        *(unsigned __int64 *)(v_rsp - 56) = a2;
        a2 = 1;
        v_stack_m30 = (unsigned int)(result);
        result = v_rsp - 56;
        *(unsigned __int64 *)(v_rsp - 40) = result;
        a4 = (unsigned __int8)(-(a4));
        *(unsigned int *)(v_rsp - 44) = a3;
        a4 = 0x54FULL;
        v_stack_m20 = 16;
        a3 = 0x21000000ULL;
        result = (unsigned int)((result) & (0x1800ULL));
        result = (unsigned int)((result) + (0x600602ULL));
        v_stack_m48 = (unsigned int)(result);
        result = EtwTraceKernelEvent(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTracePriQEnqueueWork(void *Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint32_t v_stack_m30;
    uint32_t v_stack_m48;

    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x936AE6)) ^ (local_rsp);
    v_stack_m18 = result;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xAF2EB4));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAF2EB4)))) & (8)) == 0) {
        result = *(uint32_t *)(arg1 + 0x510);
        Arg1 = local_rsp - 40;
        *(uint64_t *)(local_rsp - 0x38) = Arg2;
        Arg2 = 1;
        v_stack_m30 = (uint32_t)(result);
        result = local_rsp - 56;
        *(uint64_t *)(local_rsp - 0x28) = result;
        Arg4 = (uint8_t)(-(Arg4));
        *(uint32_t *)(local_rsp - 0x2C) = Arg3;
        Arg4 = 0x54FULL;
        v_stack_m20 = 16;
        Arg3 = 0x21000000ULL;
        result = (uint32_t)((result) & (0x1800ULL));
        result = (uint32_t)((result) + (0x600602ULL));
        v_stack_m48 = (uint32_t)(result);
        result = EtwTraceKernelEvent(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x510` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004D3C4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004D3C4C[BB_004D3C4C]
  bb_004D3C6C[BB_004D3C6C]
  bb_004D3CC0[BB_004D3CC0]
  bb_004D3CD2[BB_004D3CD2]
  bb_004D3C4C -->|branch| bb_004D3CC0
  bb_004D3C4C -->|fallthrough| bb_004D3C6C
  bb_004D3C6C -->|flow| bb_004D3CC0
```
