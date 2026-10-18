# sub_008A2BFD

- RVA: `0x008A2BFD`–`0x008A2C1D` (길이 `32` bytes)
- VA: `0x00000001408A2BFD`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007ED80`
- 디코드: `8`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008A2C0A` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008A2C0A` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008A2C17` → [sub_008A2CED](Unknown_function_008A2CED.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008A2BFD  48 8D 86 98 00 00 00            lea rax, [rsi + 0x98]
008A2C04  90                              nop
008A2C05  48 39 00                        cmp qword ptr [rax], rax
008A2C08  74 05                           je 0x1408a2c0f
008A2C0A  E8 71 00 A4 FF                  call 0x1402e2c80
008A2C0F  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
008A2C14  48 85 DB                        test rbx, rbx
008A2C17  0F 84 D0 00 00 00               je 0x1408a2ced
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008A2BFD(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;

    result = v_rsi + 152;
    if ((*(unsigned __int64 *)(v_rsi + 152)) != (v_rsi + 152)) {
        result = KiCheckForKernelApcDelivery(a1, a2, a3, a4);
    }
}
```

## 5. (Beta) C Style

```c
int64_t sub_008A2BFD(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, int64_t Arg11)
{
    int64_t result;

    result = local_rsi + 152;
    if ((*(uint64_t *)(local_rsi + 0x98)) != (local_rsi + 152)) {
        result = KiCheckForKernelApcDelivery(Arg1, Arg2, Arg3, Arg4);
    }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008A2BFD&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008A2BFD[BB_008A2BFD]
  bb_008A2C0A[BB_008A2C0A]
  bb_008A2C0F[BB_008A2C0F]
  bb_008A2BFD -->|branch| bb_008A2C0F
  bb_008A2BFD -->|fallthrough| bb_008A2C0A
  bb_008A2C0A -->|flow| bb_008A2C0F
```
