# KiGetInterruptObjectAddress

- RVA: `0x004853A0`–`0x004853B8` (길이 `24` bytes)
- VA: `0x00000001404853A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004853A0  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
004853A9  48 81 C2 00 39 00 00            add rdx, 0x3900
004853B0  8B C1                           mov eax, ecx
004853B2  48 8D 04 C2                     lea rax, [rdx + rax*8]
004853B6  C3                              ret
004853B7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiGetInterruptObjectAddress(int a1)
{
    a2 = (*(unsigned __int64 *)(gs_base + (0 + 32))) + (0x3900ULL);
    return a2 + (unsigned int)(a1) * 8;
}
```

## 5. (Beta) C Style

```c
int64_t KiGetInterruptObjectAddress(int32_t Arg1)
{
    a2 = (*(uint64_t *)(gs_base + (0 + 0x20))) + (0x3900ULL);
    return a2 + (uint32_t)(Arg1) * 8;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004853A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004853A0[BB_004853A0]
  bb_004853B7[BB_004853B7]
```
