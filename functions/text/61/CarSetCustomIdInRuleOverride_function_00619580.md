# CarSetCustomIdInRuleOverride

- RVA: `0x00619580`–`0x006195BF` (길이 `63` bytes)
- VA: `0x0000000140619580`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `20`개 명령, `63/63` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0061958F` → [CarFindRuleClassConfigurationEntryByRuleClassId](CarFindRuleClassConfigurationEntryByRuleClassId_function_0061897C.md) (function, `0x0061897C`)
- `0x006195A8` → [CarFindRuleOverrideEntryByLocalRuleId](CarFindRuleOverrideEntryByLocalRuleId_function_006189D8.md) (function, `0x006189D8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00619580  48 83 EC 28                     sub rsp, 0x28
00619584  44 8B DA                        mov r11d, edx
00619587  45 8B D0                        mov r10d, r8d
0061958A  8B D1                           mov edx, ecx
0061958C  45 33 C9                        xor r9d, r9d
0061958F  E8 E8 F3 FF FF                  call 0x14061897c
00619594  48 85 C0                        test rax, rax
00619597  75 08                           jne 0x1406195a1
00619599  41 B9 34 00 00 C0               mov r9d, 0xc0000034
0061959F  EB 15                           jmp 0x1406195b6
006195A1  48 8D 48 48                     lea rcx, [rax + 0x48]
006195A5  41 8B D3                        mov edx, r11d
006195A8  E8 2B F4 FF FF                  call 0x1406189d8
006195AD  48 85 C0                        test rax, rax
006195B0  74 E7                           je 0x140619599
006195B2  44 89 50 3C                     mov dword ptr [rax + 0x3c], r10d
006195B6  41 8B C1                        mov eax, r9d
006195B9  48 83 C4 28                     add rsp, 0x28
006195BD  C3                              ret
006195BE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CarSetCustomIdInRuleOverride(int a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a4 = 0;
    result = CarFindRuleClassConfigurationEntryByRuleClassId(a1, (unsigned int)(a1), a3, a4);
    if (result != 0) goto loc_006195A1;
loc_00619599:
    goto loc_006195B6;
loc_006195A1:
    result = CarFindRuleOverrideEntryByLocalRuleId(result + 72, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)(0xC0000034ULL));
    if (result == 0) goto loc_00619599;
    *(unsigned int *)(result + 60) = (unsigned int)((unsigned int)(a3));
loc_006195B6:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000034ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t CarSetCustomIdInRuleOverride(int32_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg4 = 0;
    result = CarFindRuleClassConfigurationEntryByRuleClassId(Arg1, (uint32_t)(Arg1), Arg3, Arg4);
    if (result != 0) goto loc_006195A1;
loc_00619599:
    goto loc_006195B6;
loc_006195A1:
    result = CarFindRuleOverrideEntryByLocalRuleId(result + 72, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)(0xC0000034ULL));
    if (result == 0) goto loc_00619599;
    *(uint32_t *)(result + 0x3C) = (uint32_t)((uint32_t)(Arg3));
loc_006195B6:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000034ULL)));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00619580&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00619580[BB_00619580]
  bb_00619599[BB_00619599]
  bb_006195A1[BB_006195A1]
  bb_006195B2[BB_006195B2]
  bb_006195B6[BB_006195B6]
  bb_006195BE[BB_006195BE]
  bb_00619580 -->|branch| bb_006195A1
  bb_00619580 -->|fallthrough| bb_00619599
  bb_00619599 -->|branch| bb_006195B6
  bb_006195A1 -->|branch| bb_00619599
  bb_006195A1 -->|fallthrough| bb_006195B2
  bb_006195B2 -->|flow| bb_006195B6
```
