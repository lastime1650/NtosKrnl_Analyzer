# sub_002F01EB

- RVA: `0x002F01EB`–`0x002F0200` (길이 `21` bytes)
- VA: `0x00000001402F01EB`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071BF0`
- 디코드: `6`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002F01EE` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002F01FB` → [sub_002F0082 + 0x4F](Unknown_function_002F0082.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002F01EB  48 8B CB                        mov rcx, rbx
002F01EE  E8 2D 64 F2 FF                  call 0x140216620
002F01F3  33 D2                           xor edx, edx
002F01F5  84 C0                           test al, al
002F01F7  48 0F 44 DA                     cmove rbx, rdx
002F01FB  E9 D1 FE FF FF                  jmp 0x1402f00d1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002F01EB(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbx;

    result = ExAcquireRundownProtection(v_rbx, a2, a3, a4);
    a2 = 0;
    if ((unsigned __int8)(result) == 0) { v_rbx = 0; }
}
```

## 5. (Beta) C Style

```c
int64_t sub_002F01EB(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rbx;

    result = ExAcquireRundownProtection(local_rbx, Arg2, a3, a4);
    Arg2 = 0;
    if ((uint8_t)(result) == 0) { local_rbx = 0; }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F01EB&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002F01EB[BB_002F01EB]
```
