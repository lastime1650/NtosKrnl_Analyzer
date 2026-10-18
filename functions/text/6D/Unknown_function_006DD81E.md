# sub_006DD81E

- RVA: `0x006DD81E`–`0x006DD832` (길이 `20` bytes)
- VA: `0x00000001406DD81E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F8A8`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006DD827` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006DD82D` → [HalpHandleMaskUnmaskSecondaryInterrupt + 0x45](../2D/HalpHandleMaskUnmaskSecondaryInterrupt_function_002D1C8C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006DD81E  48 8D 4B 78                     lea rcx, [rbx + 0x78]
006DD822  45 33 C0                        xor r8d, r8d
006DD825  33 D2                           xor edx, edx
006DD827  E8 E4 1A C6 FF                  call 0x14033f310
006DD82C  90                              nop
006DD82D  E9 9F 44 BF FF                  jmp 0x1402d1cd1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006DD81E(__int64 a1, int a2, int a3)
{
    __int64 result;

    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rbx + 120, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006DD81E(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;

    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(local_rbx + 120, Arg2, Arg3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006DD81E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006DD81E[BB_006DD81E]
```
