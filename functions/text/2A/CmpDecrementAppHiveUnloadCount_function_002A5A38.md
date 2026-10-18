# CmpDecrementAppHiveUnloadCount

- RVA: `0x002A5A38`–`0x002A5A79` (길이 `65` bytes)
- VA: `0x00000001402A5A38`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `17`개 명령, `65/65` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x002A5A6E` → [ExpUnblockPushLock](ExpUnblockPushLock_function_002A40FC.md) (function, `0x002A40FC`)

### Direct callers
- [CmpLateUnloadHiveWorker](../../page/9B/CmpLateUnloadHiveWorker_function_009B20D0.md) at `0x009B22E5`
- [CmpCompleteUnloadKey](../../page/9B/CmpCompleteUnloadKey_function_009B32FC.md) at `0x009B33B7`

### Static image references
- `0x002A5A3C` → RVA `0x00EF59A8` (`.data`; read)
- `0x002A5A44` → RVA `0x00EF59A8` (`.data`; write)
- `0x002A5A58` → RVA `0x00EF59A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002A5A38  48 83 EC 28                     sub rsp, 0x28
002A5A3C  8B 05 66 FF C4 00               mov eax, dword ptr [rip + 0xc4ff66]
002A5A42  FF C8                           dec eax
002A5A44  89 05 5E FF C4 00               mov dword ptr [rip + 0xc4ff5e], eax
002A5A4A  8B 05 58 FF C4 00               mov eax, dword ptr [rip + 0xc4ff58]
002A5A50  85 C0                           test eax, eax
002A5A52  75 1F                           jne 0x1402a5a73
002A5A54  F0 09 04 24                     lock or dword ptr [rsp], eax
002A5A58  48 83 3D 40 FF C4 00 00         cmp qword ptr [rip + 0xc4ff40], 0
002A5A60  74 11                           je 0x1402a5a73
002A5A62  45 33 C0                        xor r8d, r8d
002A5A65  48 8D 0D 34 FF C4 00            lea rcx, [rip + 0xc4ff34]
002A5A6C  33 D2                           xor edx, edx
002A5A6E  E8 89 E6 FF FF                  call 0x1402a40fc
002A5A73  48 83 C4 28                     add rsp, 0x28
002A5A77  C3                              ret
002A5A78  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpDecrementAppHiveUnloadCount(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12910438))) - 1);
    *(unsigned int *)(v_rip + 12910430) = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12910424))) != 0) goto loc_002A5A73;
    result = (unsigned int)(*(unsigned int *)(v_rip + 12910424));
    if ((*(unsigned __int64 *)(v_rip + 12910400)) != 0) {
        a3 = 0;
        a1 = v_rip + 12910388;
        a2 = 0;
        result = ExpUnblockPushLock(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpDecrementAppHiveUnloadCount(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xC4FF66))) - 1);
    *(uint32_t *)(v_rip + 0xC4FF5E) = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC4FF58))) != 0) goto loc_002A5A73;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0xC4FF58));
    if ((*(uint64_t *)(v_rip + 0xC4FF40)) != 0) {
        Arg3 = 0;
        Arg1 = v_rip + 12910388;
        Arg2 = 0;
        result = ExpUnblockPushLock(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002A5A38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002A5A38[BB_002A5A38]
  bb_002A5A54[BB_002A5A54]
  bb_002A5A62[BB_002A5A62]
  bb_002A5A73[BB_002A5A73]
  bb_002A5A78[BB_002A5A78]
  bb_002A5A38 -->|branch| bb_002A5A73
  bb_002A5A38 -->|fallthrough| bb_002A5A54
  bb_002A5A54 -->|branch| bb_002A5A73
  bb_002A5A54 -->|fallthrough| bb_002A5A62
  bb_002A5A62 -->|flow| bb_002A5A73
```
