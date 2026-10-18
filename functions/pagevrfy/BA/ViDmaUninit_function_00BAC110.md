# ViDmaUninit

- RVA: `0x00BAC110`–`0x00BAC137` (길이 `39` bytes)
- VA: `0x0000000140BAC110`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00BAC110` → RVA `0x00F03FA4` (`.data`; read/write)
- `0x00BAC117` → RVA `0x00E007F0` (`.data`; read)
- `0x00BAC120` → RVA `0x00F03FD8` (`.data`; read)
- `0x00BAC127` → RVA `0x00E00850` (`.data`; write)
- `0x00BAC12E` → RVA `0x00FF4004` (`PAGEVRFD`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAC110  83 25 8D 7E 35 00 00            and dword ptr [rip + 0x357e8d], 0
00BAC117  83 3D D2 46 25 00 3D            cmp dword ptr [rip + 0x2546d2], 0x3d
00BAC11E  72 0E                           jb 0x140bac12e
00BAC120  48 8B 05 B1 7E 35 00            mov rax, qword ptr [rip + 0x357eb1]
00BAC127  48 89 05 22 47 25 00            mov qword ptr [rip + 0x254722], rax
00BAC12E  83 25 CF 7E 44 00 00            and dword ptr [rip + 0x447ecf], 0
00BAC135  C3                              ret
00BAC136  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViDmaUninit(void)
{
    __int64 result;

    if ((*(unsigned int *)(v_rip + 2442962)) >= 61) {
        result = *(unsigned __int64 *)(v_rip + 3505841);
        *(unsigned __int64 *)(v_rip + 2443042) = result;
    }
    return result;
}
```

## 5. (Beta) C Style

```c
void ViDmaUninit(void)
{
    int64_t result;

    if ((*(uint32_t *)(v_rip + 0x2546D2)) >= 61) {
        result = *(uint64_t *)(v_rip + 0x357EB1);
        *(uint64_t *)(v_rip + 0x254722) = result;
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAC110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAC110[BB_00BAC110]
  bb_00BAC120[BB_00BAC120]
  bb_00BAC12E[BB_00BAC12E]
  bb_00BAC136[BB_00BAC136]
  bb_00BAC110 -->|branch| bb_00BAC12E
  bb_00BAC110 -->|fallthrough| bb_00BAC120
  bb_00BAC120 -->|flow| bb_00BAC12E
```
