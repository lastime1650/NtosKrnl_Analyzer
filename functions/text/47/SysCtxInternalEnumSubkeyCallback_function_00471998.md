# SysCtxInternalEnumSubkeyCallback

- RVA: `0x00471998`–`0x004719D1` (길이 `57` bytes)
- VA: `0x0000000140471998`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000ABF48`
- 디코드: `17`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004719BC` → [PnpCtxInternalEnumKeyCallback](PnpCtxInternalEnumKeyCallback_function_004719E0.md) (function, `0x004719E0`)
- `0x004719CA` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [_RegRtlEnumKeyWithCallback](../../page/99/_RegRtlEnumKeyWithCallback_function_009929EC.md) at `0x00992B71`

### Static image references
- `0x004719A7` → RVA `0x004719E0` (`PnpCtxInternalEnumKeyCallback`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00471998  48 83 EC 38                     sub rsp, 0x38
0047199C  49 8B 00                        mov rax, qword ptr [r8]
0047199F  4D 8B 50 08                     mov r10, qword ptr [r8 + 8]
004719A3  4D 8B 48 10                     mov r9, qword ptr [r8 + 0x10]
004719A7  4C 8D 05 32 00 00 00            lea r8, [rip + 0x32]
004719AE  4D 3B D0                        cmp r10, r8
004719B1  4C 8B C2                        mov r8, rdx
004719B4  48 8B D1                        mov rdx, rcx
004719B7  48 8B C8                        mov rcx, rax
004719BA  75 0B                           jne 0x1404719c7
004719BC  E8 1F 00 00 00                  call 0x1404719e0
004719C1  48 83 C4 38                     add rsp, 0x38
004719C5  C3                              ret
004719C6  CC                              int3
004719C7  49 8B C2                        mov rax, r10
004719CA  E8 01 91 24 00                  call 0x1406baad0
004719CF  EB F0                           jmp 0x1404719c1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SysCtxInternalEnumSubkeyCallback(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (56);
    if ((*(unsigned __int64 *)(a3 + 8)) != (v_rip + 50)) goto loc_004719C7;
    result = PnpCtxInternalEnumKeyCallback(*(unsigned __int64 *)(a3), a1, a2, *(unsigned __int64 *)(a3 + 16));
loc_004719C1:
    v_rsp = (v_rsp) + (56);
    return result;
loc_004719C7:
    result = guard_dispatch_icall(*(unsigned __int64 *)(a3), a1, a2, *(unsigned __int64 *)(a3 + 16));
    goto loc_004719C1;
}
```

## 5. (Beta) C Style

```c
int64_t SysCtxInternalEnumSubkeyCallback(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (56);
    if ((*(uint64_t *)(arg3 + 0x8)) != (v_rip + 50)) goto loc_004719C7;
    result = PnpCtxInternalEnumKeyCallback(*(uint64_t *)(arg3), Arg1, Arg2, *(uint64_t *)(arg3 + 0x10));
loc_004719C1:
    local_rsp = (local_rsp) + (56);
    return result;
loc_004719C7:
    result = guard_dispatch_icall(*(uint64_t *)(arg3), Arg1, Arg2, *(uint64_t *)(arg3 + 0x10));
    goto loc_004719C1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |
| `Arg3` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00471998&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00471998[BB_00471998]
  bb_004719BC[BB_004719BC]
  bb_004719C1[BB_004719C1]
  bb_004719C6[BB_004719C6]
  bb_004719C7[BB_004719C7]
  bb_00471998 -->|branch| bb_004719C7
  bb_00471998 -->|fallthrough| bb_004719BC
  bb_004719BC -->|flow| bb_004719C1
  bb_004719C6 -->|flow| bb_004719C7
  bb_004719C7 -->|branch| bb_004719C1
```
