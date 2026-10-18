# HvpDoAllocateCell

- RVA: `0x00859FB0`–`0x00859FB9` (길이 `9` bytes)
- VA: `0x0000000140859FB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0006AAB0`
- 디코드: `3`개 명령, `9/9` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HvReallocateCell](HvReallocateCell_function_0085B5D0.md) at `0x0085B6CC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00859FB0  48 8B C4                        mov rax, rsp
00859FB3  41 56                           push r14
00859FB5  48 83 EC 70                     sub rsp, 0x70
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvpDoAllocateCell(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (112);
    return v_rsp;
}
```

## 5. (Beta) C Style

```c
void HvpDoAllocateCell(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (112);
    return local_rsp;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00859FB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00859FB0[BB_00859FB0]
```
