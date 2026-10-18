# sub_002FA5CC

- RVA: `0x002FA5CC`–`0x002FA5F0` (길이 `36` bytes)
- VA: `0x00000001402FA5CC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000729D8`
- 디코드: `15`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002FA5DF` → [EtwpTraceStackWalk](EtwpTraceStackWalk_function_002F8D60.md) (function, `0x002F8D60`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002FA5CC  F7 C3 00 18 00 00               test ebx, 0x1800
002FA5D2  74 10                           je 0x1402fa5e4
002FA5D4  4C 8B CD                        mov r9, rbp
002FA5D7  4C 8B C7                        mov r8, rdi
002FA5DA  8B D3                           mov edx, ebx
002FA5DC  48 8B CE                        mov rcx, rsi
002FA5DF  E8 7C E7 FF FF                  call 0x1402f8d60
002FA5E4  48 83 C4 40                     add rsp, 0x40
002FA5E8  41 5D                           pop r13
002FA5EA  5F                              pop rdi
002FA5EB  5E                              pop rsi
002FA5EC  5D                              pop rbp
002FA5ED  5B                              pop rbx
002FA5EE  C3                              ret
002FA5EF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002FA5CC(void)
{
    __int64 result;
    __int64 v_rsp;

    if ((((unsigned int)(v_rbx)) & (0x1800ULL)) != 0) {
        a4 = v_rbp;
        a3 = v_rdi;
        a2 = (unsigned int)(v_rbx);
        a1 = v_rsi;
        result = EtwpTraceStackWalk(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
void sub_002FA5CC(void)
{
    int64_t result;
    int64_t local_rsp;

    if ((((uint32_t)(local_rbx)) & (0x1800ULL)) != 0) {
        a4 = local_rbp;
        a3 = local_rdi;
        a2 = (uint32_t)(local_rbx);
        a1 = local_rsi;
        result = EtwpTraceStackWalk(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002FA5CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002FA5CC[BB_002FA5CC]
  bb_002FA5D4[BB_002FA5D4]
  bb_002FA5E4[BB_002FA5E4]
  bb_002FA5EF[BB_002FA5EF]
  bb_002FA5CC -->|branch| bb_002FA5E4
  bb_002FA5CC -->|fallthrough| bb_002FA5D4
  bb_002FA5D4 -->|flow| bb_002FA5E4
```
