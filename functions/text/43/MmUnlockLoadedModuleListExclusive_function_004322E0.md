# MmUnlockLoadedModuleListExclusive

- RVA: `0x004322E0`–`0x00432314` (길이 `52` bytes)
- VA: `0x00000001404322E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004322F0` → [ExReleaseSpinLockExclusiveFromDpcLevel](../24/ExReleaseSpinLockExclusiveFromDpcLevel_function_002497E0.md) (function, `0x002497E0`)
- `0x00432304` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)

### Direct callers
- [MiUpdateDriverLoadInProgress](MiUpdateDriverLoadInProgress_function_004318DC.md) at `0x00431957`
- [MiUpdateDriverLoadInProgress](MiUpdateDriverLoadInProgress_function_004318DC.md) at `0x00431A38`
- [RtlRemoveInvertedFunctionTable](RtlRemoveInvertedFunctionTable_function_004320E8.md) at `0x0043210B`
- [RtlInsertInvertedFunctionTable](RtlInsertInvertedFunctionTable_function_00432138.md) at `0x00432191`
- [MiRemoveLoaderEntry](../67/MiRemoveLoaderEntry_function_006713C8.md) at `0x00671422`
- [sub_006F88AE](../6F/Unknown_function_006F88AE.md) at `0x006F8D07`

### Static image references
- `0x004322E9` → RVA `0x00FCF200` (`CACHEALI`; read)
- `0x004322F5` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004322E0  40 53                           push rbx
004322E2  48 83 EC 20                     sub rsp, 0x20
004322E6  0F B6 D9                        movzx ebx, cl
004322E9  48 8D 0D 10 CF B9 00            lea rcx, [rip + 0xb9cf10]
004322F0  E8 EB 74 E1 FF                  call 0x1402497e0
004322F5  83 3D 24 4A B9 00 00            cmp dword ptr [rip + 0xb94a24], 0
004322FC  74 0B                           je 0x140432309
004322FE  44 0F 20 C1                     mov rcx, cr8
00432302  8A D3                           mov dl, bl
00432304  E8 8F 33 0C 00                  call 0x1404f5698
00432309  44 0F 22 C3                     mov cr8, rbx
0043230D  48 83 C4 20                     add rsp, 0x20
00432311  5B                              pop rbx
00432312  C3                              ret
00432313  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmUnlockLoadedModuleListExclusive(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12177168, a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 12143140)) != 0) {
        a1 = v_cr8;
        a2 = a1;
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MmUnlockLoadedModuleListExclusive(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExReleaseSpinLockExclusiveFromDpcLevel(v_rip + 12177168, a2, a3, a4);
    if ((*(uint32_t *)(v_rip + 0xB94A24)) != 0) {
        Arg1 = v_cr8;
        a2 = Arg1;
        result = KiLowerIrqlProcessIrqlFlags(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004322E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004322E0[BB_004322E0]
  bb_004322FE[BB_004322FE]
  bb_00432309[BB_00432309]
  bb_00432313[BB_00432313]
  bb_004322E0 -->|branch| bb_00432309
  bb_004322E0 -->|fallthrough| bb_004322FE
  bb_004322FE -->|flow| bb_00432309
```
