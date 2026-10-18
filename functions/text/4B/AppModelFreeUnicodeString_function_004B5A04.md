# AppModelFreeUnicodeString

- RVA: `0x004B5A04`–`0x004B5A2D` (길이 `41` bytes)
- VA: `0x00000001404B5A04`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004B5A1B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [KIsSideloadingEnabled](../../page/7D/KIsSideloadingEnabled_function_007D9DD8.md) at `0x007D9E89`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004B5A1B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B5A04  40 53                           push rbx
004B5A06  48 83 EC 20                     sub rsp, 0x20
004B5A0A  48 8B D9                        mov rbx, rcx
004B5A0D  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
004B5A11  48 85 C9                        test rcx, rcx
004B5A14  74 10                           je 0x1404b5a26
004B5A16  BA 41 70 70 4D                  mov edx, 0x4d707041
004B5A1B  E8 50 CE 6C 00                  call 0x140b82870
004B5A20  0F 57 C0                        xorps xmm0, xmm0
004B5A23  0F 11 03                        movups xmmword ptr [rbx], xmm0
004B5A26  48 83 C4 20                     add rsp, 0x20
004B5A2A  5B                              pop rbx
004B5A2B  C3                              ret
004B5A2C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AppModelFreeUnicodeString(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 8) != 0) {
        a2 = 0x4D707041ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
        *(unsigned __int64 *)(a1) = v_xmm0;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AppModelFreeUnicodeString(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x8) != 0) {
        a2 = 0x4D707041ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x8), a2, a3, a4);
        *(uint64_t *)(arg1) = v_xmm0;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B5A04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B5A04[BB_004B5A04]
  bb_004B5A16[BB_004B5A16]
  bb_004B5A26[BB_004B5A26]
  bb_004B5A2C[BB_004B5A2C]
  bb_004B5A04 -->|branch| bb_004B5A26
  bb_004B5A04 -->|fallthrough| bb_004B5A16
  bb_004B5A16 -->|flow| bb_004B5A26
```
