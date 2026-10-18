# RtlpLogHeapDecommit

- RVA: `0x004F9EF4`–`0x004F9F6D` (길이 `121` bytes)
- VA: `0x00000001404F9EF4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AF370`
- 디코드: `26`개 명령, `121/121` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F9F55` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x004F9F62` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [RtlpHpSegPageRangeCommit](../32/RtlpHpSegPageRangeCommit_function_00325D0C.md) at `0x0032615E`

### Static image references
- `0x004F9EFB` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F9EF4  4C 8B DC                        mov r11, rsp
004F9EF7  48 83 EC 78                     sub rsp, 0x78
004F9EFB  48 8B 05 3E 08 91 00            mov rax, qword ptr [rip + 0x91083e]
004F9F02  48 33 C4                        xor rax, rsp
004F9F05  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
004F9F0A  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
004F9F0F  49 8D 43 B8                     lea rax, [r11 - 0x48]
004F9F13  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
004F9F17  41 B9 34 10 00 00               mov r9d, 0x1034
004F9F1D  83 64 24 5C 00                  and dword ptr [rsp + 0x5c], 0
004F9F22  49 89 4B B8                     mov qword ptr [r11 - 0x48], rcx
004F9F26  49 8D 4B D8                     lea rcx, [r11 - 0x28]
004F9F2A  49 89 53 C0                     mov qword ptr [r11 - 0x40], rdx
004F9F2E  BA 01 00 00 00                  mov edx, 1
004F9F33  4D 89 43 C8                     mov qword ptr [r11 - 0x38], r8
004F9F37  41 B8 20 00 00 40               mov r8d, 0x40000020
004F9F3D  C7 44 24 48 0D 00 00 00         mov dword ptr [rsp + 0x48], 0xd
004F9F45  C7 44 24 58 20 00 00 00         mov dword ptr [rsp + 0x58], 0x20
004F9F4D  C7 44 24 20 02 19 50 10         mov dword ptr [rsp + 0x20], 0x10501902
004F9F55  E8 F6 B3 D3 FF                  call 0x140235350
004F9F5A  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
004F9F5F  48 33 CC                        xor rcx, rsp
004F9F62  E8 D9 26 1B 00                  call 0x1406ac640
004F9F67  48 83 C4 78                     add rsp, 0x78
004F9F6B  C3                              ret
004F9F6C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpLogHeapDecommit(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned int v_stack_m58;

    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 9504830)) ^ (v_rsp);
    v_stack_m18 = result;
    *(unsigned __int64 *)(v_rsp - 40) = v_rsp - 72;
    *(unsigned __int64 *)(v_rsp - 72) = a1;
    *(unsigned __int64 *)(v_rsp - 64) = a2;
    *(unsigned __int64 *)(v_rsp - 56) = a3;
    v_stack_m30 = 13;
    v_stack_m20 = 32;
    v_stack_m58 = 0x10501902ULL;
    result = EtwTraceKernelEvent(v_rsp - 40, 1, (unsigned int)(0x40000020ULL), (unsigned int)(0x1034ULL));
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, (unsigned int)(0x40000020ULL), (unsigned int)(0x1034ULL));
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpLogHeapDecommit(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint32_t v_stack_m58;

    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0x91083E)) ^ (local_rsp);
    v_stack_m18 = result;
    *(uint64_t *)(local_rsp - 0x28) = local_rsp - 72;
    *(uint64_t *)(local_rsp - 0x48) = Arg1;
    *(uint64_t *)(local_rsp - 0x40) = Arg2;
    *(uint64_t *)(local_rsp - 0x38) = Arg3;
    v_stack_m30 = 13;
    v_stack_m20 = 32;
    v_stack_m58 = 0x10501902ULL;
    result = EtwTraceKernelEvent(local_rsp - 40, 1, (uint32_t)(0x40000020ULL), (uint32_t)(0x1034ULL));
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, (uint32_t)(0x40000020ULL), (uint32_t)(0x1034ULL));
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F9EF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F9EF4[BB_004F9EF4]
  bb_004F9F6C[BB_004F9F6C]
```
