# MiFreeCachedKernelShadowStackEntryCount

- RVA: `0x006863C0`–`0x006863D1` (길이 `17` bytes)
- VA: `0x00000001406863C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiCreatePartitionOffsets](../../page/7F/MiCreatePartitionOffsets_function_007FD18C.md) at `0x007FD297`

### Static image references
- `0x006863C0` → RVA `0x00FC5000` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006863C0  0F B7 05 39 EC 93 00            movzx eax, word ptr [rip + 0x93ec39]
006863C7  48 8D 04 40                     lea rax, [rax + rax*2]
006863CB  48 C1 E0 09                     shl rax, 9
006863CF  C3                              ret
006863D0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFreeCachedKernelShadowStackEntryCount(void)
{
    __int64 result;

    result = (*(unsigned __int16 *)(v_rip + 9694265) + *(unsigned __int16 *)(v_rip + 9694265) * 2) << (9);
    return result;
}
```

## 5. (Beta) C Style

```c
void MiFreeCachedKernelShadowStackEntryCount(void)
{
    int64_t result;

    result = (*(uint16_t *)(v_rip + 0x93EC39) + *(uint16_t *)(v_rip + 0x93EC39) * 2) << (9);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006863C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006863C0[BB_006863C0]
  bb_006863D0[BB_006863D0]
```
