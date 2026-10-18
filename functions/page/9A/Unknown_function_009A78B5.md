# sub_009A78B5

- RVA: `0x009A78B5`–`0x009A78D4` (길이 `31` bytes)
- VA: `0x00000001409A78B5`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009CB9C`
- 디코드: `8`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009A78C2` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009A78C2` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x009A78CE` → [sub_009A7A3D](Unknown_function_009A7A3D.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009A78B5  48 8D 8D 98 00 00 00            lea rcx, [rbp + 0x98]
009A78BC  90                              nop
009A78BD  48 39 09                        cmp qword ptr [rcx], rcx
009A78C0  74 05                           je 0x1409a78c7
009A78C2  E8 B9 B3 93 FF                  call 0x1402e2c80
009A78C7  48 8B 6C 24 78                  mov rbp, qword ptr [rsp + 0x78]
009A78CC  85 FF                           test edi, edi
009A78CE  0F 88 69 01 00 00               js 0x1409a7a3d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009A78B5(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15)
{
    __int64 result;

    if ((*(unsigned __int64 *)(v_rbp + 152)) != (v_rbp + 152)) {
        result = KiCheckForKernelApcDelivery(v_rbp + 152, a2, a3, a4);
    }
}
```

## 5. (Beta) C Style

```c
int64_t sub_009A78B5(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, int64_t Arg15)
{
    int64_t result;

    if ((*(uint64_t *)(local_rbp + 0x98)) != (local_rbp + 152)) {
        result = KiCheckForKernelApcDelivery(local_rbp + 152, Arg2, Arg3, Arg4);
    }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A78B5&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A78B5[BB_009A78B5]
  bb_009A78C2[BB_009A78C2]
  bb_009A78C7[BB_009A78C7]
  bb_009A78B5 -->|branch| bb_009A78C7
  bb_009A78B5 -->|fallthrough| bb_009A78C2
  bb_009A78C2 -->|flow| bb_009A78C7
```
