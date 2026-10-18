# CmpVolumeManagerInitialize

- RVA: `0x007E8B38`–`0x007E8B57` (길이 `31` bytes)
- VA: `0x00000001407E8B38`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmInitSystem1](../../init/C5/CmInitSystem1_function_00C559CC.md) at `0x00C55C6D`

### Static image references
- `0x007E8B38` → RVA `0x00FDA418` (`PAGEDATA`; read/write)
- `0x007E8B40` → RVA `0x00FDA420` (`PAGEDATA`; read)
- `0x007E8B47` → RVA `0x00FDA428` (`PAGEDATA`; write)
- `0x007E8B4E` → RVA `0x00FDA420` (`PAGEDATA`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E8B38  48 83 25 D8 18 7F 00 00         and qword ptr [rip + 0x7f18d8], 0
007E8B40  48 8D 05 D9 18 7F 00            lea rax, [rip + 0x7f18d9]
007E8B47  48 89 05 DA 18 7F 00            mov qword ptr [rip + 0x7f18da], rax
007E8B4E  48 89 05 CB 18 7F 00            mov qword ptr [rip + 0x7f18cb], rax
007E8B55  C3                              ret
007E8B56  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpVolumeManagerInitialize(void)
{
    *(unsigned __int64 *)(v_rip + 8329434) = v_rip + 8329433;
    *(unsigned __int64 *)(v_rip + 8329419) = v_rip + 8329433;
    return v_rip + 8329433;
}
```

## 5. (Beta) C Style

```c
void CmpVolumeManagerInitialize(void)
{
    *(uint64_t *)(v_rip + 0x7F18DA) = v_rip + 8329433;
    *(uint64_t *)(v_rip + 0x7F18CB) = v_rip + 8329433;
    return v_rip + 8329433;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E8B38&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007E8B38[BB_007E8B38]
  bb_007E8B56[BB_007E8B56]
```
