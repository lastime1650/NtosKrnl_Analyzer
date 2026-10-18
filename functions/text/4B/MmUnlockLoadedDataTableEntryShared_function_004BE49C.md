# MmUnlockLoadedDataTableEntryShared

- RVA: `0x004BE49C`–`0x004BE4D0` (길이 `52` bytes)
- VA: `0x00000001404BE49C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068784`
- 디코드: `13`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BE4A5` → [MiUnlockLoaderEntry](../2A/MiUnlockLoaderEntry_function_002A3E28.md) (function, `0x002A3E28`)
- `0x004BE4BA` → [MiReleaseLoadLock](../2A/MiReleaseLoadLock_function_002A3CD0.md) (function, `0x002A3CD0`)

### Direct callers
- [ExpQuerySingleModuleInformation](../../page/7C/ExpQuerySingleModuleInformation_function_007C4FB0.md) at `0x007C5020`
- [RtlPcToFilePath](../../page/A2/RtlPcToFilePath_function_00A2B9A0.md) at `0x00A2B9C9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BE49C  48 83 EC 28                     sub rsp, 0x28
004BE4A0  BA 02 00 00 00                  mov edx, 2
004BE4A5  E8 7E 59 DE FF                  call 0x1402a3e28
004BE4AA  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
004BE4B3  48 85 C9                        test rcx, rcx
004BE4B6  74 0D                           je 0x1404be4c5
004BE4B8  33 D2                           xor edx, edx
004BE4BA  E8 11 58 DE FF                  call 0x1402a3cd0
004BE4BF  48 83 C4 28                     add rsp, 0x28
004BE4C3  C3                              ret
004BE4C4  CC                              int3
004BE4C5  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
004BE4CE  EB E8                           jmp 0x1404be4b8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmUnlockLoadedDataTableEntryShared(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiUnlockLoaderEntry(a1, 2, a3, a4);
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) == 0) goto loc_004BE4C5;
loc_004BE4B8:
    a2 = 0;
    result = MiReleaseLoadLock(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
loc_004BE4C5:
    goto loc_004BE4B8;
}
```

## 5. (Beta) C Style

```c
void MmUnlockLoadedDataTableEntryShared(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiUnlockLoaderEntry(a1, 2, a3, a4);
    if (*(uint64_t *)(gs_base + (0 + 0x188)) == 0) goto loc_004BE4C5;
loc_004BE4B8:
    a2 = 0;
    result = MiReleaseLoadLock(*(uint64_t *)(gs_base + (0 + 0x188)), a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
loc_004BE4C5:
    goto loc_004BE4B8;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BE49C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BE49C[BB_004BE49C]
  bb_004BE4B8[BB_004BE4B8]
  bb_004BE4C4[BB_004BE4C4]
  bb_004BE4C5[BB_004BE4C5]
  bb_004BE49C -->|branch| bb_004BE4C5
  bb_004BE49C -->|fallthrough| bb_004BE4B8
  bb_004BE4C4 -->|flow| bb_004BE4C5
  bb_004BE4C5 -->|branch| bb_004BE4B8
```
