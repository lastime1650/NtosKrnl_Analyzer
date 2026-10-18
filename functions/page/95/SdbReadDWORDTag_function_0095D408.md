# SdbReadDWORDTag

- RVA: `0x0095D408`–`0x0095D49E` (길이 `150` bytes)
- VA: `0x000000014095D408`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00092D90`
- 디코드: `40`개 명령, `150/150` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **16**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0095D424` → [SdbGetTagFromTagID](SdbGetTagFromTagID_function_0095E3C0.md) (function, `0x0095E3C0`)
- `0x0095D44B` → [SdbpReadTagData](SdbpReadTagData_function_0095E170.md) (function, `0x0095E170`)
- `0x0095D46C` → [SdbGetTagFromTagID](SdbGetTagFromTagID_function_0095E3C0.md) (function, `0x0095E3C0`)
- `0x0095D495` → [AslLogCallPrintf](AslLogCallPrintf_function_0095E4EC.md) (function, `0x0095E4EC`)

### Direct callers
- [SdbpCheckApplicationTypeAttributes](../../text/69/SdbpCheckApplicationTypeAttributes_function_0069C93C.md) at `0x0069CBA7`
- [KsepDbGetShimInfo](../74/KsepDbGetShimInfo_function_00748E94.md) at `0x0074900B`
- [KsepDbReadKData](../74/KsepDbReadKData_function_0074923C.md) at `0x007492BA`
- [KsepDbReadKData](../74/KsepDbReadKData_function_0074923C.md) at `0x00749344`
- [SdbQueryDataExTagID](../81/SdbQueryDataExTagID_function_008136E0.md) at `0x00813897`
- [SdbQueryDataExTagID](../81/SdbQueryDataExTagID_function_008136E0.md) at `0x008139A9`
- [SdbpCheckContainment](../81/SdbpCheckContainment_function_00813D30.md) at `0x00813D96`
- [SdbpCheckOSKind](../81/SdbpCheckOSKind_function_00815330.md) at `0x0081534D`
- [SdbpCheckRuntimePlatform](../81/SdbpCheckRuntimePlatform_function_00815460.md) at `0x00815488`
- [SdbpGetDeviceDWORD](../81/SdbpGetDeviceDWORD_function_008159B0.md) at `0x008159DE`
- [SdbpGetExeEntryFlags](../81/SdbpGetExeEntryFlags_function_00815A00.md) at `0x00815AD9`
- [SdbpGetExeEntryFlags](../81/SdbpGetExeEntryFlags_function_00815A00.md) at `0x00815B03`
- [SdbpGetMatchingTextAttributes](../81/SdbpGetMatchingTextAttributes_function_00815B38.md) at `0x00815C9C`
- [SdbpGetMatchingTextAttributes](../81/SdbpGetMatchingTextAttributes_function_00815B38.md) at `0x00815CD4`
- [SdbpGetRegistryMatchingAttributes](../81/SdbpGetRegistryMatchingAttributes_function_00815D5C.md) at `0x00815E5F`
- [SdbpGetRegistryMatchingAttributes](../81/SdbpGetRegistryMatchingAttributes_function_00815D5C.md) at `0x00815F94`
- [SdbpCheckAllAttributes](../81/SdbpCheckAllAttributes_function_008187EC.md) at `0x00818933`
- [SdbMergeIsEntryUpdated](../81/SdbMergeIsEntryUpdated_function_00819158.md) at `0x008193A7`
- [KsepDbGetDriverShimsInternal](KsepDbGetDriverShimsInternal_function_009597C4.md) at `0x009599B3`
- [SdbGetDatabaseEdition](SdbGetDatabaseEdition_function_0095BBE4.md) at `0x0095BC20`
- [InitOnceScanIndexes](InitOnceScanIndexes_function_0095D4C0.md) at `0x0095D5EB`

### Static image references
- `0x0095D474` → RVA `0x000128B0` (`.rdata`; read)
- `0x0095D47F` → RVA `0x000128A0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0095D408  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0095D40D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0095D412  57                              push rdi
0095D413  48 83 EC 30                     sub rsp, 0x30
0095D417  41 8B F8                        mov edi, r8d
0095D41A  44 89 44 24 50                  mov dword ptr [rsp + 0x50], r8d
0095D41F  8B DA                           mov ebx, edx
0095D421  48 8B F1                        mov rsi, rcx
0095D424  E8 97 0F 00 00                  call 0x14095e3c0
0095D429  B9 00 F0 00 00                  mov ecx, 0xf000
0095D42E  8B D3                           mov edx, ebx
0095D430  66 23 C1                        and ax, cx
0095D433  B9 00 40 00 00                  mov ecx, 0x4000
0095D438  66 3B C1                        cmp ax, cx
0095D43B  48 8B CE                        mov rcx, rsi
0095D43E  75 2C                           jne 0x14095d46c
0095D440  41 B9 04 00 00 00               mov r9d, 4
0095D446  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
0095D44B  E8 20 0D 00 00                  call 0x14095e170
0095D450  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
0095D454  85 C0                           test eax, eax
0095D456  0F 44 CF                        cmove ecx, edi
0095D459  8B C1                           mov eax, ecx
0095D45B  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
0095D460  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
0095D465  48 83 C4 30                     add rsp, 0x30
0095D469  5F                              pop rdi
0095D46A  C3                              ret
0095D46B  CC                              int3
0095D46C  E8 4F 0F 00 00                  call 0x14095e3c0
0095D471  0F B7 C0                        movzx eax, ax
0095D474  4C 8D 0D 35 54 6B FF            lea r9, [rip - 0x94abcb]
0095D47B  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0095D47F  48 8D 15 1A 54 6B FF            lea rdx, [rip - 0x94abe6]
0095D486  41 B8 B3 00 00 00               mov r8d, 0xb3
0095D48C  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0095D490  B9 01 00 00 00                  mov ecx, 1
0095D495  E8 52 10 00 00                  call 0x14095e4ec
0095D49A  8B C7                           mov eax, edi
0095D49C  EB BD                           jmp 0x14095d45b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SdbReadDWORDTag(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_stack_p18 = a3;
    result = SdbGetTagFromTagID(a1, a2, a3, a4);
    result = (unsigned __int16)((result) & ((unsigned __int16)((unsigned int)(0xF000ULL))));
    if (((unsigned __int16)(result)) != ((unsigned __int16)((unsigned int)(0x4000ULL)))) goto loc_0095D46C;
    result = SdbpReadTagData(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_p18, 4);
    a1 = (unsigned int)(v_stack_p18);
    if ((unsigned int)(result) == 0) { a1 = (unsigned int)((unsigned int)(a3)); }
loc_0095D45B:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)(a1));
loc_0095D46C:
    result = SdbGetTagFromTagID(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), v_stack_p18, 4);
    v_stack_p28 = (unsigned int)((unsigned __int16)(result));
    v_stack_p20 = (unsigned int)(v_stack_p8);
    result = AslLogCallPrintf(1, v_rip - 9743334, 179, v_rip - 9743307);
    goto loc_0095D45B;
}
```

## 5. (Beta) C Style

```c
int64_t SdbReadDWORDTag(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (48);
    v_stack_p18 = Arg3;
    result = SdbGetTagFromTagID(Arg1, Arg2, Arg3, a4);
    result = (uint16_t)((result) & ((uint16_t)((uint32_t)(0xF000ULL))));
    if (((uint16_t)(result)) != ((uint16_t)((uint32_t)(0x4000ULL)))) goto loc_0095D46C;
    result = SdbpReadTagData(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_p18, 4);
    Arg1 = (uint32_t)(v_stack_p18);
    if ((uint32_t)(result) == 0) { Arg1 = (uint32_t)((uint32_t)(Arg3)); }
loc_0095D45B:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)(Arg1));
loc_0095D46C:
    result = SdbGetTagFromTagID(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_stack_p18, 4);
    v_stack_p28 = (uint32_t)((uint16_t)(result));
    v_stack_p20 = (uint32_t)(v_stack_p8);
    result = AslLogCallPrintf(1, v_rip - 9743334, 179, v_rip - 9743307);
    goto loc_0095D45B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0095D408&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0095D408[BB_0095D408]
  bb_0095D440[BB_0095D440]
  bb_0095D45B[BB_0095D45B]
  bb_0095D46B[BB_0095D46B]
  bb_0095D46C[BB_0095D46C]
  bb_0095D408 -->|branch| bb_0095D46C
  bb_0095D408 -->|fallthrough| bb_0095D440
  bb_0095D440 -->|flow| bb_0095D45B
  bb_0095D46B -->|flow| bb_0095D46C
  bb_0095D46C -->|branch| bb_0095D45B
```
