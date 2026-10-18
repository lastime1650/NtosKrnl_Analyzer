# BCryptOpenAlgorithmProvider

- RVA: `0x00ABF200`–`0x00ABF27F` (길이 `127` bytes)
- VA: `0x0000000140ABF200`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `34`개 명령, `127/127` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00ABF231` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (function, `0x00428814`)
- `0x00ABF24E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00ABF25C` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (function, `0x00456DC0`)

### Direct callers
- [SecureDump_EncryptSymmetricKeyWithPublicKey](../../text/5A/SecureDump_EncryptSymmetricKeyWithPublicKey_function_005A27A4.md) at `0x005A289D`
- [SecureDump_SymmetricEncryptionSetup](../../text/5A/SecureDump_SymmetricEncryptionSetup_function_005A3774.md) at `0x005A37AB`
- [SmCrEncStart](../7A/SmCrEncStart_function_007AA208.md) at `0x007AA240`
- [sub_00811D74](../81/Unknown_function_00811D74.md) at `0x00811DDE`
- [RtlGenerateClass5Guid](../AC/RtlGenerateClass5Guid_function_00AC4510.md) at `0x00AC45A3`

### Static image references
- `0x00ABF21F` → RVA `0x00F04E30` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00ABF231` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (`PAGE` → `.text`)
  - `0x00ABF24E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00ABF25C` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ABF200  48 8B C4                        mov rax, rsp
00ABF203  48 89 58 08                     mov qword ptr [rax + 8], rbx
00ABF207  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00ABF20B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00ABF20F  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00ABF213  41 56                           push r14
00ABF215  48 83 EC 30                     sub rsp, 0x30
00ABF219  4C 8B F1                        mov r14, rcx
00ABF21C  41 8B F9                        mov edi, r9d
00ABF21F  48 8B 0D 0A 5C 44 00            mov rcx, qword ptr [rip + 0x445c0a]
00ABF226  49 8B F0                        mov rsi, r8
00ABF229  48 8B EA                        mov rbp, rdx
00ABF22C  BB 02 00 00 C0                  mov ebx, 0xc0000002
00ABF231  E8 DE 95 96 FF                  call 0x140428814
00ABF236  48 85 C0                        test rax, rax
00ABF239  74 26                           je 0x140abf261
00ABF23B  48 8B 80 C8 00 00 00            mov rax, qword ptr [rax + 0xc8]
00ABF242  44 8B CF                        mov r9d, edi
00ABF245  4C 8B C6                        mov r8, rsi
00ABF248  48 8B D5                        mov rdx, rbp
00ABF24B  49 8B CE                        mov rcx, r14
00ABF24E  E8 7D B8 BF FF                  call 0x1406baad0
00ABF253  48 8B 0D D6 5B 44 00            mov rcx, qword ptr [rip + 0x445bd6]
00ABF25A  8B D8                           mov ebx, eax
00ABF25C  E8 5F 7B 99 FF                  call 0x140456dc0
00ABF261  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00ABF266  8B C3                           mov eax, ebx
00ABF268  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00ABF26D  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00ABF272  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00ABF277  48 83 C4 30                     add rsp, 0x30
00ABF27B  41 5E                           pop r14
00ABF27D  C3                              ret
00ABF27E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BCryptOpenAlgorithmProvider(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    result = ExGetExtensionTable(*(unsigned __int64 *)(v_rip + 4480010), a2, a3, a4);
    v_rbx = (unsigned int)(0xC0000002ULL);
    if (result != 0) {
        result = *(unsigned __int64 *)(result + 200);
        a4 = (unsigned int)((unsigned int)(a4));
        a3 = a3;
        a2 = a2;
        a1 = a1;
        result = guard_dispatch_icall(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rip + 4479958);
        v_rbx = (unsigned int)(result);
        result = ExReleaseExtensionTable(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t BCryptOpenAlgorithmProvider(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    result = ExGetExtensionTable(*(uint64_t *)(v_rip + 0x445C0A), Arg2, Arg3, Arg4);
    local_rbx = (uint32_t)(0xC0000002ULL);
    if (result != 0) {
        result = *(uint64_t *)(result + 0xC8);
        Arg4 = (uint32_t)((uint32_t)(Arg4));
        Arg3 = Arg3;
        Arg2 = Arg2;
        Arg1 = Arg1;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(v_rip + 0x445BD6);
        local_rbx = (uint32_t)(result);
        result = ExReleaseExtensionTable(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ABF200&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ABF200[BB_00ABF200]
  bb_00ABF23B[BB_00ABF23B]
  bb_00ABF261[BB_00ABF261]
  bb_00ABF27E[BB_00ABF27E]
  bb_00ABF200 -->|branch| bb_00ABF261
  bb_00ABF200 -->|fallthrough| bb_00ABF23B
  bb_00ABF23B -->|flow| bb_00ABF261
```
