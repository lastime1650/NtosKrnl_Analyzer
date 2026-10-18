# sub_00857E9A

- RVA: `0x00857E9A`–`0x00857EB2` (길이 `24` bytes)
- VA: `0x0000000140857E9A`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006A6DC`
- 디코드: `6`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00857EA8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00857EA8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00857E9D` → [sub_00857CAB + 0x5](Unknown_function_00857CAB.md) (`tail-transfer`)
  - `0x00857EAD` → [sub_00857864 + 0x45](Unknown_function_00857864.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00857E9A  45 33 E4                        xor r12d, r12d
00857E9D  E9 0E FE FF FF                  jmp 0x140857cb0
00857EA2  48 8B 4D C0                     mov rcx, qword ptr [rbp - 0x40]
00857EA6  33 D2                           xor edx, edx
00857EA8  E8 C3 A9 32 00                  call 0x140b82870
00857EAD  E9 F7 F9 FF FF                  jmp 0x1408578a9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00857E9A(__int64 a1, int a2)
{
    __int64 v_r12;

    v_r12 = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00857E9A(int64_t Arg1, int32_t Arg2)
{
    int64_t local_r12;

    local_r12 = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00857E9A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00857E9A[BB_00857E9A]
  bb_00857EA2[BB_00857EA2]
```
