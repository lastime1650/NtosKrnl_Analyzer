# PspGetFullAttribute

- RVA: `0x005E34E0`–`0x005E34F0` (길이 `16` bytes)
- VA: `0x00000001405E34E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `16/16` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PspBuildCreateProcessContext](../../page/9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EEDBA`

### Static image references
- `0x005E34E3` → RVA `0x0002B830` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E34E0  0F B7 C1                        movzx eax, cx
005E34E3  48 8D 0D 46 83 A4 FF            lea rcx, [rip - 0x5b7cba]
005E34EA  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
005E34EE  C3                              ret
005E34EF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspGetFullAttribute(unsigned __int16 a1)
{
    return *(unsigned __int64 *)(v_rip - 5995706 + a1 * 8);
}
```

## 5. (Beta) C Style

```c
int64_t PspGetFullAttribute(uint16_t Arg1)
{
    return *(uint64_t *)(v_rip - 0x5B7CBA + Arg1 * 8);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E34E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E34E0[BB_005E34E0]
  bb_005E34EF[BB_005E34EF]
```
