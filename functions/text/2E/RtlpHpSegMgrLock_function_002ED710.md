# RtlpHpSegMgrLock

- RVA: `0x002ED710`–`0x002ED72C` (길이 `28` bytes)
- VA: `0x00000001402ED710`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002ED721` → [RtlpHpAcquireLockExclusive](../32/RtlpHpAcquireLockExclusive_function_003246B0.md) (function, `0x003246B0`)

### Direct callers
- [RtlpHpSegMgrVaCtxAlloc](RtlpHpSegMgrVaCtxAlloc_function_002ED384.md) at `0x002ED3D2`
- [RtlpHpSegMgrVaCtxInsert](RtlpHpSegMgrVaCtxInsert_function_002ED470.md) at `0x002ED4D5`
- [RtlpHpSegMgrVaCtxFree](RtlpHpSegMgrVaCtxFree_function_002ED570.md) at `0x002ED5D5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002ED710  48 83 EC 28                     sub rsp, 0x28
002ED714  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
002ED717  48 83 C1 70                     add rcx, 0x70
002ED71B  0F B6 D0                        movzx edx, al
002ED71E  83 E2 01                        and edx, 1
002ED721  E8 8A 6F 03 00                  call 0x1403246b0
002ED726  48 83 C4 28                     add rsp, 0x28
002ED72A  C3                              ret
002ED72B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpSegMgrLock(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (a1) + (112);
    a2 = (unsigned int)(((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 40)))) & (1));
    result = RtlpHpAcquireLockExclusive(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpSegMgrLock(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (Arg1) + (112);
    a2 = (uint32_t)(((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) & (1));
    result = RtlpHpAcquireLockExclusive(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002ED710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002ED710[BB_002ED710]
  bb_002ED72B[BB_002ED72B]
```
