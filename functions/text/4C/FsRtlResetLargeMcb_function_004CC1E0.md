# FsRtlResetLargeMcb

- RVA: `0x004CC1E0`–`0x004CC20E` (길이 `46` bytes)
- VA: `0x00000001404CC1E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068804`
- 디코드: `16`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004CC1FB` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x004CC207` → [ExReleaseFastMutex](../25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004CC1E0  40 53                           push rbx
004CC1E2  48 83 EC 20                     sub rsp, 0x20
004CC1E6  48 8B D9                        mov rbx, rcx
004CC1E9  84 D2                           test dl, dl
004CC1EB  74 0B                           je 0x1404cc1f8
004CC1ED  83 61 0C 00                     and dword ptr [rcx + 0xc], 0
004CC1F1  48 83 C4 20                     add rsp, 0x20
004CC1F5  5B                              pop rbx
004CC1F6  C3                              ret
004CC1F7  CC                              int3
004CC1F8  48 8B 09                        mov rcx, qword ptr [rcx]
004CC1FB  E8 A0 23 D4 FF                  call 0x14020e5a0
004CC200  48 8B 0B                        mov rcx, qword ptr [rbx]
004CC203  83 63 0C 00                     and dword ptr [rbx + 0xc], 0
004CC207  E8 B4 57 D8 FF                  call 0x1402519c0
004CC20C  EB E3                           jmp 0x1404cc1f1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlResetLargeMcb(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (a2 == 0) goto loc_004CC1F8;
loc_004CC1F1:
    v_rsp = (v_rsp) + (32);
    return result;
loc_004CC1F8:
    result = ExAcquireFastMutex(*(unsigned __int64 *)(a1), a2, a3, a4);
    result = ExReleaseFastMutex(*(unsigned __int64 *)(a1), a2, a3, a4);
    goto loc_004CC1F1;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlResetLargeMcb(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (Arg2 == 0) goto loc_004CC1F8;
loc_004CC1F1:
    local_rsp = (local_rsp) + (32);
    return result;
loc_004CC1F8:
    result = ExAcquireFastMutex(*(uint64_t *)(arg1), Arg2, a3, a4);
    result = ExReleaseFastMutex(*(uint64_t *)(arg1), Arg2, a3, a4);
    goto loc_004CC1F1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004CC1E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004CC1E0[BB_004CC1E0]
  bb_004CC1ED[BB_004CC1ED]
  bb_004CC1F1[BB_004CC1F1]
  bb_004CC1F7[BB_004CC1F7]
  bb_004CC1F8[BB_004CC1F8]
  bb_004CC1E0 -->|branch| bb_004CC1F8
  bb_004CC1E0 -->|fallthrough| bb_004CC1ED
  bb_004CC1ED -->|flow| bb_004CC1F1
  bb_004CC1F7 -->|flow| bb_004CC1F8
  bb_004CC1F8 -->|branch| bb_004CC1F1
```
