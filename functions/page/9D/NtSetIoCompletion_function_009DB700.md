# NtSetIoCompletion

- RVA: `0x009DB700`–`0x009DB7A1` (길이 `161` bytes)
- VA: `0x00000001409DB700`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F874`
- 디코드: `41`개 명령, `161/161` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009DB74A` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x009DB778` → [IoSetIoCompletionEx](../../text/24/IoSetIoCompletionEx_function_0024FA80.md) (function, `0x0024FA80`)
- `0x009DB784` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x009DB72D` → RVA `0x00FC6CC0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009DB778` → [IoSetIoCompletionEx](../../text/24/IoSetIoCompletionEx_function_0024FA80.md) (`PAGE` → `.text`)
  - `0x009DB784` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009DB700  4C 8B DC                        mov r11, rsp
009DB703  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
009DB707  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
009DB70B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
009DB70F  57                              push rdi
009DB710  48 83 EC 50                     sub rsp, 0x50
009DB714  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009DB71D  33 ED                           xor ebp, ebp
009DB71F  41 8B F9                        mov edi, r9d
009DB722  49 89 6B D0                     mov qword ptr [r11 - 0x30], rbp
009DB726  49 8B F0                        mov rsi, r8
009DB729  49 89 6B E8                     mov qword ptr [r11 - 0x18], rbp
009DB72D  4C 8B 05 8C B5 5E 00            mov r8, qword ptr [rip + 0x5eb58c]
009DB734  48 8B DA                        mov rbx, rdx
009DB737  44 0F B6 88 32 02 00 00         movzx r9d, byte ptr [rax + 0x232]
009DB73F  8D 55 02                        lea edx, [rbp + 2]
009DB742  49 8D 43 E8                     lea rax, [r11 - 0x18]
009DB746  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
009DB74A  E8 61 D6 E8 FF                  call 0x140868db0
009DB74F  85 C0                           test eax, eax
009DB751  78 38                           js 0x1409db78b
009DB753  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
009DB75B  44 8B CF                        mov r9d, edi
009DB75E  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009DB763  4C 8B C6                        mov r8, rsi
009DB766  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
009DB76B  48 8B D3                        mov rdx, rbx
009DB76E  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
009DB773  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009DB778  E8 03 43 87 FF                  call 0x14024fa80
009DB77D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009DB782  8B D8                           mov ebx, eax
009DB784  E8 C7 DB 91 FF                  call 0x1402f9350
009DB789  8B C3                           mov eax, ebx
009DB78B  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
009DB790  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
009DB795  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
009DB79A  48 83 C4 50                     add rsp, 0x50
009DB79E  5F                              pop rdi
009DB79F  C3                              ret
009DB7A0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetIoCompletion(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (80);
    v_rbp = 0;
    *(unsigned __int64 *)(v_rsp - 48) = 0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    *(unsigned __int64 *)(v_rsp - 56) = v_rsp - 24;
    result = ObReferenceObjectByHandle(a1, v_rbp + 2, *(unsigned __int64 *)(v_rip + 6206860), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_rbx = a2;
    if (!(sign_flag)) {
        result = a5;
        a4 = (unsigned int)((unsigned int)(a4));
        a1 = v_stack_m18;
        a3 = a3;
        v_stack_m28 = 0;
        a2 = a2;
        v_stack_m30 = 1;
        v_stack_m38 = result;
        result = IoSetIoCompletionEx(a1, a2, a3, a4);
        a1 = v_stack_m18;
        v_rbx = (unsigned int)(result);
        result = ObfDereferenceObject(a1, a2, a3, a4);
        result = (unsigned int)(v_rbx);
    }
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetIoCompletion(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint8_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (80);
    local_rbp = 0;
    *(uint64_t *)(local_rsp - 0x30) = 0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    *(uint64_t *)(local_rsp - 0x38) = local_rsp - 24;
    result = ObReferenceObjectByHandle(Arg1, local_rbp + 2, *(uint64_t *)(v_rip + 0x5EB58C), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    local_rbx = Arg2;
    if (!(sign_flag)) {
        result = Arg5;
        Arg4 = (uint32_t)((uint32_t)(Arg4));
        Arg1 = v_stack_m18;
        Arg3 = Arg3;
        v_stack_m28 = 0;
        Arg2 = Arg2;
        v_stack_m30 = 1;
        v_stack_m38 = result;
        result = IoSetIoCompletionEx(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m18;
        local_rbx = (uint32_t)(result);
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, Arg4);
        result = (uint32_t)(local_rbx);
    }
    local_rsp = (local_rsp) + (80);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009DB700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009DB700[BB_009DB700]
  bb_009DB753[BB_009DB753]
  bb_009DB78B[BB_009DB78B]
  bb_009DB7A0[BB_009DB7A0]
  bb_009DB700 -->|branch| bb_009DB78B
  bb_009DB700 -->|fallthrough| bb_009DB753
  bb_009DB753 -->|flow| bb_009DB78B
```
