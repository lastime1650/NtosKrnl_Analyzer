# SdbReadWORDTag

- RVA: `0x0095D898`–`0x0095D934` (길이 `156` bytes)
- VA: `0x000000014095D898`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00092DDC`
- 디코드: `40`개 명령, `156/156` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0095D8B6` → [SdbGetTagFromTagID](SdbGetTagFromTagID_function_0095E3C0.md) (function, `0x0095E3C0`)
- `0x0095D8DD` → [SdbpReadTagData](SdbpReadTagData_function_0095E170.md) (function, `0x0095E170`)
- `0x0095D901` → [SdbGetTagFromTagID](SdbGetTagFromTagID_function_0095E3C0.md) (function, `0x0095E3C0`)
- `0x0095D92A` → [AslLogCallPrintf](AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)

### Direct callers
- [SdbpCheckAllAttributes](../81/SdbpCheckAllAttributes_function_008187EC.md) at `0x0081894F`
- [SdbMergeIsEntryUpdated](../81/SdbMergeIsEntryUpdated_function_00819158.md) at `0x00819322`
- [SdbMergeIsEntryUpdated](../81/SdbMergeIsEntryUpdated_function_00819158.md) at `0x0081934D`
- [InitOnceScanIndexes](InitOnceScanIndexes_function_0095D4C0.md) at `0x0095D57F`
- [InitOnceScanIndexes](InitOnceScanIndexes_function_0095D4C0.md) at `0x0095D5B7`
- [SdbpCheckForMatch](../AB/SdbpCheckForMatch_function_00AB37BC.md) at `0x00AB388F`

### Static image references
- `0x0095D909` → RVA `0x000128B0` (`.rdata`; read)
- `0x0095D914` → RVA `0x0003D288` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0095D898  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0095D89D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0095D8A2  57                              push rdi
0095D8A3  48 83 EC 30                     sub rsp, 0x30
0095D8A7  41 0F B7 F8                     movzx edi, r8w
0095D8AB  66 44 89 44 24 50               mov word ptr [rsp + 0x50], r8w
0095D8B1  8B DA                           mov ebx, edx
0095D8B3  48 8B F1                        mov rsi, rcx
0095D8B6  E8 05 0B 00 00                  call 0x14095e3c0
0095D8BB  B9 00 F0 00 00                  mov ecx, 0xf000
0095D8C0  8B D3                           mov edx, ebx
0095D8C2  66 23 C1                        and ax, cx
0095D8C5  B9 00 30 00 00                  mov ecx, 0x3000
0095D8CA  66 3B C1                        cmp ax, cx
0095D8CD  48 8B CE                        mov rcx, rsi
0095D8D0  75 2F                           jne 0x14095d901
0095D8D2  41 B9 02 00 00 00               mov r9d, 2
0095D8D8  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
0095D8DD  E8 8E 08 00 00                  call 0x14095e170
0095D8E2  0F B7 4C 24 50                  movzx ecx, word ptr [rsp + 0x50]
0095D8E7  85 C0                           test eax, eax
0095D8E9  66 0F 44 CF                     cmove cx, di
0095D8ED  0F B7 C1                        movzx eax, cx
0095D8F0  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0095D8F5  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
0095D8FA  48 83 C4 30                     add rsp, 0x30
0095D8FE  5F                              pop rdi
0095D8FF  C3                              ret
0095D900  CC                              int3
0095D901  E8 BA 0A 00 00                  call 0x14095e3c0
0095D906  0F B7 C0                        movzx eax, ax
0095D909  4C 8D 0D A0 4F 6B FF            lea r9, [rip - 0x94b060]
0095D910  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0095D914  48 8D 15 6D F9 6D FF            lea rdx, [rip - 0x920693]
0095D91B  41 B8 AC 00 00 00               mov r8d, 0xac
0095D921  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0095D925  B9 01 00 00 00                  mov ecx, 1
0095D92A  E8 BD 0B 00 00                  call 0x14095e4ec
0095D92F  0F B7 C7                        movzx eax, di
0095D932  EB BC                           jmp 0x14095d8f0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SdbReadWORDTag(__int64 a1, int a2, unsigned __int16 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int16 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_stack_p18 = a3;
    result = SdbGetTagFromTagID(a1, a2, a3, a4);
    result = (unsigned __int16)((result) & ((unsigned __int16)((unsigned int)(0xF000ULL))));
    if (((unsigned __int16)(result)) != ((unsigned __int16)((unsigned int)(0x3000ULL)))) goto loc_0095D901;
    result = SdbpReadTagData(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_p18, 2);
    a1 = v_stack_p18;
    if ((unsigned int)(result) == 0) { a1 = a3; }
loc_0095D8F0:
    v_rsp = (v_rsp) + (48);
    return (unsigned __int16)(a1);
loc_0095D901:
    result = SdbGetTagFromTagID(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_p18, 2);
    v_stack_p28 = (unsigned int)((unsigned __int16)(result));
    v_stack_p20 = (unsigned int)(v_stack_p8);
    result = AslLogCallPrintf(1, v_rip - 9569939, 172, v_rip - 9744480);
    goto loc_0095D8F0;
}
```

## 5. (Beta) C Style

```c
int64_t SdbReadWORDTag(int64_t Arg1, int32_t Arg2, uint16_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint16_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (48);
    v_stack_p18 = Arg3;
    result = SdbGetTagFromTagID(Arg1, Arg2, Arg3, a4);
    result = (uint16_t)((result) & ((uint16_t)((uint32_t)(0xF000ULL))));
    if (((uint16_t)(result)) != ((uint16_t)((uint32_t)(0x3000ULL)))) goto loc_0095D901;
    result = SdbpReadTagData(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_p18, 2);
    Arg1 = v_stack_p18;
    if ((uint32_t)(result) == 0) { Arg1 = Arg3; }
loc_0095D8F0:
    local_rsp = (local_rsp) + (48);
    return (uint16_t)(Arg1);
loc_0095D901:
    result = SdbGetTagFromTagID(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_p18, 2);
    v_stack_p28 = (uint32_t)((uint16_t)(result));
    v_stack_p20 = (uint32_t)(v_stack_p8);
    result = AslLogCallPrintf(1, v_rip - 9569939, 172, v_rip - 9744480);
    goto loc_0095D8F0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0095D898&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0095D898[BB_0095D898]
  bb_0095D8D2[BB_0095D8D2]
  bb_0095D8F0[BB_0095D8F0]
  bb_0095D900[BB_0095D900]
  bb_0095D901[BB_0095D901]
  bb_0095D898 -->|branch| bb_0095D901
  bb_0095D898 -->|fallthrough| bb_0095D8D2
  bb_0095D8D2 -->|flow| bb_0095D8F0
  bb_0095D900 -->|flow| bb_0095D901
  bb_0095D901 -->|branch| bb_0095D8F0
```
