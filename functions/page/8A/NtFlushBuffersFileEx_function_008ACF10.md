# NtFlushBuffersFileEx

- RVA: `0x008ACF10`–`0x008ACF9D` (길이 `141` bytes)
- VA: `0x00000001408ACF10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F83C`
- 디코드: `36`개 명령, `141/141` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008ACF50` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (function, `0x0029D530`)
- `0x008ACF87` → [IopFlushBuffersFile](IopFlushBuffersFile_function_008ACFA4.md) (function, `0x008ACFA4`)

### Direct callers
- [NtFlushBuffersFile](NtFlushBuffersFile_function_008ACEE0.md) at `0x008ACEF1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008ACF50` → [IopReferenceFileObject](../../text/29/IopReferenceFileObject_function_0029D530.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008ACF10  4C 8B DC                        mov r11, rsp
008ACF13  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
008ACF17  49 89 73 10                     mov qword ptr [r11 + 0x10], rsi
008ACF1B  57                              push rdi
008ACF1C  48 83 EC 50                     sub rsp, 0x50
008ACF20  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008ACF29  49 8B F8                        mov rdi, r8
008ACF2C  49 83 63 F0 00                  and qword ptr [r11 - 0x10], 0
008ACF31  41 8B D9                        mov ebx, r9d
008ACF34  49 83 63 E8 00                  and qword ptr [r11 - 0x18], 0
008ACF39  4D 8D 4B F0                     lea r9, [r11 - 0x10]
008ACF3D  8B F2                           mov esi, edx
008ACF3F  33 D2                           xor edx, edx
008ACF41  44 8A 80 32 02 00 00            mov r8b, byte ptr [rax + 0x232]
008ACF48  49 8D 43 E8                     lea rax, [r11 - 0x18]
008ACF4C  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
008ACF50  E8 DB 05 9F FF                  call 0x14029d530
008ACF55  85 C0                           test eax, eax
008ACF57  78 33                           js 0x1408acf8c
008ACF59  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
008ACF61  44 8B CB                        mov r9d, ebx
008ACF64  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008ACF69  4C 8B C7                        mov r8, rdi
008ACF6C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008ACF71  8B D6                           mov edx, esi
008ACF73  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
008ACF79  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
008ACF7F  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
008ACF83  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008ACF87  E8 18 00 00 00                  call 0x1408acfa4
008ACF8C  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
008ACF91  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
008ACF96  48 83 C4 50                     add rsp, 0x50
008ACF9A  5F                              pop rdi
008ACF9B  C3                              ret
008ACF9C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtFlushBuffersFileEx(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    v_rsp = (v_rsp) - (80);
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 56) = v_rsp - 24;
    result = IopReferenceFileObject(a1, a2, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), v_rsp - 16);
    if (!(sign_flag)) {
        result = a5;
        a4 = (unsigned int)((unsigned int)(a4));
        a1 = v_stack_m10;
        a3 = a3;
        v_stack_m20 = result;
        a2 = (unsigned int)((unsigned int)(a2));
        result = v_stack_m14;
        v_stack_m38 = (unsigned int)(result);
        result = IopFlushBuffersFile(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtFlushBuffersFileEx(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    local_rsp = (local_rsp) - (80);
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x38) = local_rsp - 24;
    result = IopReferenceFileObject(Arg1, Arg2, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), local_rsp - 16);
    if (!(sign_flag)) {
        result = Arg5;
        Arg4 = (uint32_t)((uint32_t)(Arg4));
        Arg1 = v_stack_m10;
        Arg3 = Arg3;
        v_stack_m20 = result;
        Arg2 = (uint32_t)((uint32_t)(Arg2));
        result = v_stack_m14;
        v_stack_m38 = (uint32_t)(result);
        result = IopFlushBuffersFile(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (80);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008ACF10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008ACF10[BB_008ACF10]
  bb_008ACF59[BB_008ACF59]
  bb_008ACF8C[BB_008ACF8C]
  bb_008ACF9C[BB_008ACF9C]
  bb_008ACF10 -->|branch| bb_008ACF8C
  bb_008ACF10 -->|fallthrough| bb_008ACF59
  bb_008ACF59 -->|flow| bb_008ACF8C
```
