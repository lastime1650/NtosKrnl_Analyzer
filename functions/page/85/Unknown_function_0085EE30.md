# sub_0085EE30

- RVA: `0x0085EE30`–`0x0085EE44` (길이 `20` bytes)
- VA: `0x000000014085EE30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B2C0`
- 디코드: `7`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0085EE38` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0085EE38` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0085EE40` → [sub_0085EDFE](Unknown_function_0085EDFE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0085EE30  48 8B CF                        mov rcx, rdi
0085EE33  33 D2                           xor edx, edx
0085EE35  48 8B 3F                        mov rdi, qword ptr [rdi]
0085EE38  E8 33 3A 32 00                  call 0x140b82870
0085EE3D  48 85 FF                        test rdi, rdi
0085EE40  74 BC                           je 0x14085edfe
0085EE42  EB EC                           jmp 0x14085ee30
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0085EE30(__int64 a1, int a2)
{
    __int64 result;

    a2 = 0;
    result = ExFreePoolWithTag(v_rdi, a2, a3, a4);
    goto loc_0085EE30;
}
```

## 5. (Beta) C Style

```c
int64_t sub_0085EE30(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    Arg2 = 0;
    result = ExFreePoolWithTag(local_rdi, Arg2, a3, a4);
    goto loc_0085EE30;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085EE30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0085EE30[BB_0085EE30]
  bb_0085EE42[BB_0085EE42]
  bb_0085EE30 -->|fallthrough| bb_0085EE42
  bb_0085EE42 -->|branch| bb_0085EE30
```
