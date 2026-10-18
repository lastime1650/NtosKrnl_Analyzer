# HalpMmAllocCtxInit

- RVA: `0x005448BC`–`0x005448DB` (길이 `31` bytes)
- VA: `0x00000001405448BC`
- 실행 섹션: `.text`
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
- [HalpMmInitSystem](../../pagelk/B5/HalpMmInitSystem_function_00B5DA60.md) at `0x00B5DB38`

### Static image references
- `0x005448BC` → RVA `0x00FC2CB0` (`.data`; read/write)
- `0x005448C4` → RVA `0x00FC2CA0` (`.data`; read)
- `0x005448CB` → RVA `0x00FC2CA8` (`.data`; write)
- `0x005448D2` → RVA `0x00FC2CA0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005448BC  48 83 25 EC E3 A7 00 00         and qword ptr [rip + 0xa7e3ec], 0
005448C4  48 8D 05 D5 E3 A7 00            lea rax, [rip + 0xa7e3d5]
005448CB  48 89 05 D6 E3 A7 00            mov qword ptr [rip + 0xa7e3d6], rax
005448D2  48 89 05 C7 E3 A7 00            mov qword ptr [rip + 0xa7e3c7], rax
005448D9  C3                              ret
005448DA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpMmAllocCtxInit(void)
{
    *(unsigned __int64 *)(v_rip + 11002838) = v_rip + 11002837;
    *(unsigned __int64 *)(v_rip + 11002823) = v_rip + 11002837;
    return v_rip + 11002837;
}
```

## 5. (Beta) C Style

```c
void HalpMmAllocCtxInit(void)
{
    *(uint64_t *)(v_rip + 0xA7E3D6) = v_rip + 11002837;
    *(uint64_t *)(v_rip + 0xA7E3C7) = v_rip + 11002837;
    return v_rip + 11002837;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005448BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005448BC[BB_005448BC]
  bb_005448DA[BB_005448DA]
```
