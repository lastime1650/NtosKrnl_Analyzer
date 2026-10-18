# sub_0031ED9E

- RVA: `0x0031ED9E`–`0x0031EDB1` (길이 `19` bytes)
- VA: `0x000000014031ED9E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000752A4`
- 디코드: `10`개 명령, `19/19` bytes 표시
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
0031ED9E  48 81 C4 90 00 00 00            add rsp, 0x90
0031EDA5  41 5F                           pop r15
0031EDA7  41 5E                           pop r14
0031EDA9  41 5C                           pop r12
0031EDAB  5F                              pop rdi
0031EDAC  5E                              pop rsi
0031EDAD  5D                              pop rbp
0031EDAE  5B                              pop rbx
0031EDAF  C3                              ret
0031EDB0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0031ED9E(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) + (144);
    return;
}
```

## 5. (Beta) C Style

```c
void sub_0031ED9E(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) + (144);
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0031ED9E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0031ED9E[BB_0031ED9E]
  bb_0031EDB0[BB_0031EDB0]
```
