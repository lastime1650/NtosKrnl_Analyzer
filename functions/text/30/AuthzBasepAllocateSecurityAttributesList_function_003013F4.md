# AuthzBasepAllocateSecurityAttributesList

- RVA: `0x003013F4`–`0x0030143E` (길이 `74` bytes)
- VA: `0x00000001403013F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `22`개 명령, `74/74` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00301403` → [AuthzBasepMemAlloc](../2F/AuthzBasepMemAlloc_function_002FFD90.md) (function, `0x002FFD90`)

### Direct callers
- [sub_003A7C07](../3A/Unknown_function_003A7C07.md) at `0x003A7C3A`
- [SepVerifyDesktopAppxPackageName](../3A/SepVerifyDesktopAppxPackageName_function_003A9728.md) at `0x003A98A4`
- [SepSetUserClaimAttributesToken](../../page/7A/SepSetUserClaimAttributesToken_function_007A36C0.md) at `0x007A3710`
- [AuthzBasepInitializeSystemSecurityAttributes](../../page/82/AuthzBasepInitializeSystemSecurityAttributes_function_00821E08.md) at `0x00821E62`
- [SepDuplicateClaimAttributes](../../page/A7/SepDuplicateClaimAttributes_function_00A76334.md) at `0x00A76398`
- [SepDuplicateClaimAttributes](../../page/A7/SepDuplicateClaimAttributes_function_00A76334.md) at `0x00A76447`
- [sub_00B3F630](../../page/B3/Unknown_function_00B3F630.md) at `0x00B3F63A`
- [sub_00B3F630](../../page/B3/Unknown_function_00B3F630.md) at `0x00B3F689`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003013F4  48 83 EC 28                     sub rsp, 0x28
003013F8  B9 30 00 00 00                  mov ecx, 0x30
003013FD  41 B8 53 65 41 74               mov r8d, 0x74416553
00301403  E8 88 E9 FF FF                  call 0x1402ffd90
00301408  33 D2                           xor edx, edx
0030140A  48 85 C0                        test rax, rax
0030140D  74 29                           je 0x140301438
0030140F  89 50 04                        mov dword ptr [rax + 4], edx
00301412  48 8D 48 08                     lea rcx, [rax + 8]
00301416  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
0030141A  89 50 1C                        mov dword ptr [rax + 0x1c], edx
0030141D  48 89 50 28                     mov qword ptr [rax + 0x28], rdx
00301421  48 89 49 08                     mov qword ptr [rcx + 8], rcx
00301425  48 89 09                        mov qword ptr [rcx], rcx
00301428  48 8D 48 20                     lea rcx, [rax + 0x20]
0030142C  89 10                           mov dword ptr [rax], edx
0030142E  48 89 49 08                     mov qword ptr [rcx + 8], rcx
00301432  48 89 09                        mov qword ptr [rcx], rcx
00301435  89 50 18                        mov dword ptr [rax + 0x18], edx
00301438  48 83 C4 28                     add rsp, 0x28
0030143C  C3                              ret
0030143D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AuthzBasepAllocateSecurityAttributesList(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = AuthzBasepMemAlloc(48, a2, (unsigned int)(0x74416553ULL), a4);
    a2 = 0;
    if (result != 0) {
        *(unsigned int *)(result + 4) = 0;
        a1 = result + 8;
        *(unsigned __int64 *)(result + 16) = 0;
        *(unsigned int *)(result + 28) = 0;
        *(unsigned __int64 *)(result + 40) = 0;
        *(unsigned __int64 *)(a1 + 8) = a1;
        *(unsigned __int64 *)(a1) = a1;
        a1 = result + 32;
        *(unsigned int *)(result) = 0;
        *(unsigned __int64 *)(a1 + 8) = a1;
        *(unsigned __int64 *)(a1) = a1;
        *(unsigned int *)(result + 24) = 0;
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AuthzBasepAllocateSecurityAttributesList(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = AuthzBasepMemAlloc(48, Arg2, (uint32_t)(0x74416553ULL), a4);
    Arg2 = 0;
    if (result != 0) {
        *(uint32_t *)(result + 0x4) = 0;
        Arg1 = result + 8;
        *(uint64_t *)(result + 0x10) = 0;
        *(uint32_t *)(result + 0x1C) = 0;
        *(uint64_t *)(result + 0x28) = 0;
        *(uint64_t *)(Arg1 + 0x8) = Arg1;
        *(uint64_t *)(Arg1) = Arg1;
        Arg1 = result + 32;
        *(uint32_t *)(result) = 0;
        *(uint64_t *)(Arg1 + 0x8) = Arg1;
        *(uint64_t *)(Arg1) = Arg1;
        *(uint32_t *)(result + 0x18) = 0;
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003013F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003013F4[BB_003013F4]
  bb_0030140F[BB_0030140F]
  bb_00301438[BB_00301438]
  bb_0030143D[BB_0030143D]
  bb_003013F4 -->|branch| bb_00301438
  bb_003013F4 -->|fallthrough| bb_0030140F
  bb_0030140F -->|flow| bb_00301438
```
