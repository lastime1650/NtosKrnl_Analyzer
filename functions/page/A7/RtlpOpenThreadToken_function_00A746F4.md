# RtlpOpenThreadToken

- RVA: `0x00A746F4`–`0x00A7474A` (길이 `86` bytes)
- VA: `0x0000000140A746F4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007DDD4`
- 디코드: `25`개 명령, `86/86` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A7471A` → [ZwOpenThreadTokenEx](../../text/6A/ZwOpenThreadTokenEx_function_006AD6B0.md) (function, `0x006AD6B0`)
- `0x00A74743` → [ZwOpenThreadTokenEx](../../text/6A/ZwOpenThreadTokenEx_function_006AD6B0.md) (function, `0x006AD6B0`)

### Direct callers
- [RtlAcquirePrivilege](../87/RtlAcquirePrivilege_function_00879120.md) at `0x008791BF`
- [RtlAcquirePrivilege](../87/RtlAcquirePrivilege_function_00879120.md) at `0x00879348`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A7471A` → [ZwOpenThreadTokenEx](../../text/6A/ZwOpenThreadTokenEx_function_006AD6B0.md) (`PAGE` → `.text`)
  - `0x00A74743` → [ZwOpenThreadTokenEx](../../text/6A/ZwOpenThreadTokenEx_function_006AD6B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A746F4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A746F9  57                              push rdi
00A746FA  48 83 EC 30                     sub rsp, 0x30
00A746FE  48 8B DA                        mov rbx, rdx
00A74701  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00A74706  8B D1                           mov edx, ecx
00A74708  8B F9                           mov edi, ecx
00A7470A  48 C7 C1 FE FF FF FF            mov rcx, 0xfffffffffffffffe
00A74711  41 B9 00 02 00 00               mov r9d, 0x200
00A74717  41 B0 01                        mov r8b, 1
00A7471A  E8 91 8F C3 FF                  call 0x1406ad6b0
00A7471F  85 C0                           test eax, eax
00A74721  78 0C                           js 0x140a7472f
00A74723  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00A74728  48 83 C4 30                     add rsp, 0x30
00A7472C  5F                              pop rdi
00A7472D  C3                              ret
00A7472E  CC                              int3
00A7472F  45 33 C0                        xor r8d, r8d
00A74732  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A74737  41 B9 00 02 00 00               mov r9d, 0x200
00A7473D  8B D7                           mov edx, edi
00A7473F  49 8D 48 FE                     lea rcx, [r8 - 2]
00A74743  E8 68 8F C3 FF                  call 0x1406ad6b0
00A74748  EB D9                           jmp 0x140a74723
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpOpenThreadToken(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_stack_m18 = a2;
    result = ZwOpenThreadTokenEx(-2, (unsigned int)(a1), 1, 512);
    if (sign_flag) goto loc_00A7472F;
loc_00A74723:
    v_rsp = (v_rsp) + (48);
    return result;
loc_00A7472F:
    a3 = 0;
    v_stack_p20 = v_stack_p8;
    result = ZwOpenThreadTokenEx(a3 - 2, (unsigned int)((unsigned int)((unsigned int)(a1))), a3, 512);
    goto loc_00A74723;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpOpenThreadToken(int32_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    v_stack_m18 = Arg2;
    result = ZwOpenThreadTokenEx(-2, (uint32_t)(Arg1), 1, 512);
    if (sign_flag) goto loc_00A7472F;
loc_00A74723:
    local_rsp = (local_rsp) + (48);
    return result;
loc_00A7472F:
    a3 = 0;
    v_stack_p20 = v_stack_p8;
    result = ZwOpenThreadTokenEx(a3 - 2, (uint32_t)((uint32_t)((uint32_t)(Arg1))), a3, 512);
    goto loc_00A74723;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A746F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A746F4[BB_00A746F4]
  bb_00A74723[BB_00A74723]
  bb_00A7472E[BB_00A7472E]
  bb_00A7472F[BB_00A7472F]
  bb_00A746F4 -->|branch| bb_00A7472F
  bb_00A746F4 -->|fallthrough| bb_00A74723
  bb_00A7472E -->|flow| bb_00A7472F
  bb_00A7472F -->|branch| bb_00A74723
```
