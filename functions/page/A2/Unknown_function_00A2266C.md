# sub_00A2266C

- RVA: `0x00A2266C`–`0x00A22678` (길이 `12` bytes)
- VA: `0x0000000140A2266C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `12/12` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_008D379C](../8D/Unknown_function_008D379C.md) at `0x008D3A1F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A2266C  48 85 C9                        test rcx, rcx
00A2266F  74 05                           je 0x140a22676
00A22671  F0 48 FF 41 08                  lock inc qword ptr [rcx + 8]
00A22676  C3                              ret
00A22677  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00A2266C(__int64 a1)
{
    if (a1 != 0) {
    }
    return;
}
```

## 5. (Beta) C Style

```c
void sub_00A2266C(int64_t Arg1)
{
    if (Arg1 != 0) {
    }
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A2266C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A2266C[BB_00A2266C]
  bb_00A22671[BB_00A22671]
  bb_00A22676[BB_00A22676]
  bb_00A22677[BB_00A22677]
  bb_00A2266C -->|branch| bb_00A22676
  bb_00A2266C -->|fallthrough| bb_00A22671
  bb_00A22671 -->|flow| bb_00A22676
```
