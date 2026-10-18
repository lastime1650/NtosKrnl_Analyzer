# KiQuantumEnd

- RVA: `0x0021BA90`–`0x0021BAB5` (길이 `37` bytes)
- VA: `0x000000014021BA90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005EDA4`
- 디코드: `12`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_0021B9AC](Unknown_function_0021B9AC.md) at `0x0021B9B3`
- [KiIdleLoop](../6B/KiIdleLoop_function_006B2910.md) at `0x006B29BF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0021BA90  48 8B C4                        mov rax, rsp
0021BA93  55                              push rbp
0021BA94  53                              push rbx
0021BA95  57                              push rdi
0021BA96  41 54                           push r12
0021BA98  41 56                           push r14
0021BA9A  41 57                           push r15
0021BA9C  48 8D 68 A1                     lea rbp, [rax - 0x5f]
0021BAA0  48 81 EC E8 00 00 00            sub rsp, 0xe8
0021BAA7  65 4C 8B 24 25 20 00 00 00      mov r12, qword ptr gs:[0x20]
0021BAB0  33 FF                           xor edi, edi
0021BAB2  45 32 FF                        xor r15b, r15b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiQuantumEnd(void)
{
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (232);
    v_rdi = 0;
    v_r15 = 0;
    return v_rsp;
}
```

## 5. (Beta) C Style

```c
void KiQuantumEnd(void)
{
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (232);
    local_rdi = 0;
    local_r15 = 0;
    return local_rsp;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0021BA90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0021BA90[BB_0021BA90]
```
