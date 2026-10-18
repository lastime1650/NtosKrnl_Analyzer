# CmSiProcessTupleInitialize

- RVA: `0x0066DC24`–`0x0066DC3E` (길이 `26` bytes)
- VA: `0x000000014066DC24`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmpInitializeRegistryProcess](../../page/7E/CmpInitializeRegistryProcess_function_007E8180.md) at `0x007E81A9`

### Static image references
- `0x0066DC27` → RVA `0x00EF7200` (`.data`; read)
- `0x0066DC2E` → RVA `0x00EF7210` (`.data`; read)
- `0x0066DC35` → RVA `0x00EF7220` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066DC24  0F 57 C0                        xorps xmm0, xmm0
0066DC27  0F 11 05 D2 95 88 00            movups xmmword ptr [rip + 0x8895d2], xmm0
0066DC2E  0F 11 05 DB 95 88 00            movups xmmword ptr [rip + 0x8895db], xmm0
0066DC35  0F 11 05 E4 95 88 00            movups xmmword ptr [rip + 0x8895e4], xmm0
0066DC3C  C3                              ret
0066DC3D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall CmSiProcessTupleInitialize(void)
{
    *(unsigned __int64 *)(v_rip + 8951250) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 8951259) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 8951268) = v_xmm0;
    return;
}
```

## 5. (Beta) C Style

```c
void CmSiProcessTupleInitialize(void)
{
    *(uint64_t *)(v_rip + 0x8895D2) = v_xmm0;
    *(uint64_t *)(v_rip + 0x8895DB) = v_xmm0;
    *(uint64_t *)(v_rip + 0x8895E4) = v_xmm0;
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066DC24&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066DC24[BB_0066DC24]
  bb_0066DC3D[BB_0066DC3D]
```
