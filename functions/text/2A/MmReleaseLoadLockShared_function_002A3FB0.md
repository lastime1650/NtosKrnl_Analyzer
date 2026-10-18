# MmReleaseLoadLockShared

- RVA: `0x002A3FB0`–`0x002A3FD1` (길이 `33` bytes)
- VA: `0x00000001402A3FB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068784`
- 디코드: `10`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002A3FBB` → [MiReleaseLoadLock](MiReleaseLoadLock_function_002A3CD0.md) (function, `0x002A3CD0`)

### Direct callers
- [MiLockLoadedDataTableEntry](MiLockLoadedDataTableEntry_function_002A38F4.md) at `0x002A3940`
- [MiEnumerateSystemImages](MiEnumerateSystemImages_function_002A3D40.md) at `0x002A3DCC`
- [FsRtlSetDriverBacking](../../page/71/FsRtlSetDriverBacking_function_00716310.md) at `0x0071636F`
- [MiSplitDriverPage](../../page/7F/MiSplitDriverPage_function_007F8EB8.md) at `0x007F8F2E`
- [MmFreeDriverInitialization](../../page/A4/MmFreeDriverInitialization_function_00A4AD08.md) at `0x00A4AD3C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A3FB0  48 83 EC 28                     sub rsp, 0x28
002A3FB4  48 85 C9                        test rcx, rcx
002A3FB7  74 0D                           je 0x1402a3fc6
002A3FB9  33 D2                           xor edx, edx
002A3FBB  E8 10 FD FF FF                  call 0x1402a3cd0
002A3FC0  48 83 C4 28                     add rsp, 0x28
002A3FC4  C3                              ret
002A3FC5  CC                              int3
002A3FC6  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002A3FCF  EB E8                           jmp 0x1402a3fb9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmReleaseLoadLockShared(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 == 0) goto loc_002A3FC6;
loc_002A3FB9:
    a2 = 0;
    result = MiReleaseLoadLock(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
loc_002A3FC6:
    goto loc_002A3FB9;
}
```

## 5. (Beta) C Style

```c
int64_t MmReleaseLoadLockShared(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 == 0) goto loc_002A3FC6;
loc_002A3FB9:
    Arg2 = 0;
    result = MiReleaseLoadLock(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
loc_002A3FC6:
    goto loc_002A3FB9;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A3FB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A3FB0[BB_002A3FB0]
  bb_002A3FB9[BB_002A3FB9]
  bb_002A3FC5[BB_002A3FC5]
  bb_002A3FC6[BB_002A3FC6]
  bb_002A3FB0 -->|branch| bb_002A3FC6
  bb_002A3FB0 -->|fallthrough| bb_002A3FB9
  bb_002A3FC5 -->|flow| bb_002A3FC6
  bb_002A3FC6 -->|branch| bb_002A3FB9
```
