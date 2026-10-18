# PopEsInStandbyAcDcCallback

- RVA: `0x00769830`–`0x00769863` (길이 `51` bytes)
- VA: `0x0000000140769830`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0076983B` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00769840` → [PopEsInStandbyEvaluate](../A4/PopEsInStandbyEvaluate_function_00A4A260.md) (function, `0x00A4A260`)
- `0x0076984A` → [PopEsWorkItemSchedule](../A4/PopEsWorkItemSchedule_function_00A4A5DC.md) (function, `0x00A4A5DC`)
- `0x00769856` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00769834` → RVA `0x00F08440` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0076983B` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00769856` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00769830  48 83 EC 28                     sub rsp, 0x28
00769834  48 8D 0D 05 EC 79 00            lea rcx, [rip + 0x79ec05]
0076983B  E8 04 73 CC FF                  call 0x140430b44
00769840  E8 1B 0A 2E 00                  call 0x140a4a260
00769845  B9 02 00 00 00                  mov ecx, 2
0076984A  E8 8D 0D 2E 00                  call 0x140a4a5dc
0076984F  48 8D 0D EA EB 79 00            lea rcx, [rip + 0x79ebea]
00769856  E8 61 63 B7 FF                  call 0x1402dfbbc
0076985B  33 C0                           xor eax, eax
0076985D  48 83 C4 28                     add rsp, 0x28
00769861  C3                              ret
00769862  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopEsInStandbyAcDcCallback(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PopAcquireRwLockExclusive(v_rip + 7990277, a2, a3, a4);
    result = PopEsInStandbyEvaluate(v_rip + 7990277, a2, a3, a4);
    result = PopEsWorkItemSchedule(2, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 7990250, a2, a3, a4);
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopEsInStandbyAcDcCallback(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PopAcquireRwLockExclusive(v_rip + 7990277, a2, a3, a4);
    result = PopEsInStandbyEvaluate(v_rip + 7990277, a2, a3, a4);
    result = PopEsWorkItemSchedule(2, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 7990250, a2, a3, a4);
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00769830&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00769830[BB_00769830]
  bb_00769862[BB_00769862]
```
