# VfIsVerifierExtensionEnabled

- RVA: `0x006121FC`–`0x00612204` (길이 `8` bytes)
- VA: `0x00000001406121FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `3`개 명령, `8/8` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopMarkComponentsBootPhase](../../pagelk/B6/PopMarkComponentsBootPhase_function_00B6E0E4.md) at `0x00B6E245`
- [VfNotifyOfHibernate](../../pagevrfy/B9/VfNotifyOfHibernate_function_00B97618.md) at `0x00B97651`

### Static image references
- `0x006121FC` → RVA `0x00FFDA18` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006121FC  8B 05 16 B8 9E 00               mov eax, dword ptr [rip + 0x9eb816]
00612202  C3                              ret
00612203  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfIsVerifierExtensionEnabled(void)
{
    return (unsigned int)(*(unsigned int *)(v_rip + 10401814));
}
```

## 5. (Beta) C Style

```c
void VfIsVerifierExtensionEnabled(void)
{
    return (uint32_t)(*(uint32_t *)(v_rip + 0x9EB816));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006121FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006121FC[BB_006121FC]
  bb_00612203[BB_00612203]
```
