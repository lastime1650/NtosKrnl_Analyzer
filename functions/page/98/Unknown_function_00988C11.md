# sub_00988C11

- RVA: `0x00988C11`–`0x00988C44` (길이 `51` bytes)
- VA: `0x0000000140988C11`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097E6C`
- 디코드: `12`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00988C18` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00988C35` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00988C11` → RVA `0x00E2D728` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00988C18` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00988C35` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00988C3F` → [MiReturnImageBase + 0x13](MiReturnImageBase_function_00988B00.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00988C11  48 8D 0D 10 4B 4A 00            lea rcx, [rip + 0x4a4b10]
00988C18  E8 E3 89 95 FF                  call 0x1402e1600
00988C1D  90                              nop
00988C1E  66 83 86 E6 01 00 00 01         add word ptr [rsi + 0x1e6], 1
00988C26  75 12                           jne 0x140988c3a
00988C28  48 8D 86 98 00 00 00            lea rax, [rsi + 0x98]
00988C2F  90                              nop
00988C30  48 39 00                        cmp qword ptr [rax], rax
00988C33  74 05                           je 0x140988c3a
00988C35  E8 46 A0 95 FF                  call 0x1402e2c80
00988C3A  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00988C3F  E9 CF FE FF FF                  jmp 0x140988b13
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00988C11(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;

    result = KeAbPostRelease(v_rip + 4868880, a2, a3, a4);
    if (condition_is_not_equal) goto loc_00988C3A;
    result = v_rsi + 152;
    if ((*(unsigned __int64 *)(v_rsi + 152)) != (v_rsi + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 4868880, a2, a3, a4);
    }
}
```

## 5. (Beta) C Style

```c
int64_t sub_00988C11(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, int64_t Arg9)
{
    int64_t result;

    result = KeAbPostRelease(v_rip + 4868880, Arg2, Arg3, Arg4);
    if (condition_is_not_equal) goto loc_00988C3A;
    result = local_rsi + 152;
    if ((*(uint64_t *)(local_rsi + 0x98)) != (local_rsi + 152)) {
        result = KiCheckForKernelApcDelivery(v_rip + 4868880, Arg2, Arg3, Arg4);
    }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00988C11&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00988C11[BB_00988C11]
  bb_00988C28[BB_00988C28]
  bb_00988C35[BB_00988C35]
  bb_00988C3A[BB_00988C3A]
  bb_00988C11 -->|branch| bb_00988C3A
  bb_00988C11 -->|fallthrough| bb_00988C28
  bb_00988C28 -->|branch| bb_00988C3A
  bb_00988C28 -->|fallthrough| bb_00988C35
  bb_00988C35 -->|flow| bb_00988C3A
```
