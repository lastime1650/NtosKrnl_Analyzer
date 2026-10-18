# sub_00343167

- RVA: `0x00343167`–`0x00343173` (길이 `12` bytes)
- VA: `0x0000000140343167`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00077A90`
- 디코드: `7`개 명령, `12/12` bytes 표시
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
00343167  48 83 C4 28                     add rsp, 0x28
0034316B  41 5F                           pop r15
0034316D  41 5E                           pop r14
0034316F  5F                              pop rdi
00343170  5B                              pop rbx
00343171  C3                              ret
00343172  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00343167(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) + (40);
    return;
}
```

## 5. (Beta) C Style

```c
void sub_00343167(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) + (40);
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00343167&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00343167[BB_00343167]
  bb_00343172[BB_00343172]
```
