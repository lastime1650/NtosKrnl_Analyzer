# sub_0038D011

- RVA: `0x0038D011`–`0x0038D025` (길이 `20` bytes)
- VA: `0x000000014038D011`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000803B8`
- 디코드: `9`개 명령, `20/20` bytes 표시
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
0038D011  B8 7E 00 00 C0                  mov eax, 0xc000007e
0038D016  48 83 C4 60                     add rsp, 0x60
0038D01A  41 5F                           pop r15
0038D01C  41 5E                           pop r14
0038D01E  41 5D                           pop r13
0038D020  41 5C                           pop r12
0038D022  5E                              pop rsi
0038D023  C3                              ret
0038D024  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0038D011(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) + (96);
    return (unsigned int)(0xC000007EULL);
}
```

## 5. (Beta) C Style

```c
void sub_0038D011(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) + (96);
    return (uint32_t)(0xC000007EULL);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0038D011&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0038D011[BB_0038D011]
  bb_0038D024[BB_0038D024]
```
