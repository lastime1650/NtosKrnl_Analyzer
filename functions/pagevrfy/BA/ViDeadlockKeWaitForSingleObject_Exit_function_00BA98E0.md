# ViDeadlockKeWaitForSingleObject_Exit

- RVA: `0x00BA98E0`–`0x00BA9908` (길이 `40` bytes)
- VA: `0x0000000140BA98E0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BA98FD` → [ViDeadlockObjectAcquired](ViDeadlockObjectAcquired_function_00BA9AD4.md) (function, `0x00BA9AD4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA98E0  48 83 EC 28                     sub rsp, 0x28
00BA98E4  F7 41 20 7F FF FF FF            test dword ptr [rcx + 0x20], 0xffffff7f
00BA98EB  75 15                           jne 0x140ba9902
00BA98ED  4C 8B 09                        mov r9, qword ptr [rcx]
00BA98F0  48 8D 51 18                     lea rdx, [rcx + 0x18]
00BA98F4  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
00BA98F8  B9 01 00 00 00                  mov ecx, 1
00BA98FD  E8 D2 01 00 00                  call 0x140ba9ad4
00BA9902  48 83 C4 28                     add rsp, 0x28
00BA9906  C3                              ret
00BA9907  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViDeadlockKeWaitForSingleObject_Exit(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((*(unsigned int *)(a1 + 32)) & (0xFFFFFF7FULL)) == 0) {
        a4 = *(unsigned __int64 *)(a1);
        a2 = a1 + 24;
        a3 = *(unsigned __int64 *)(a1 + 8);
        a1 = 1;
        result = ViDeadlockObjectAcquired(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViDeadlockKeWaitForSingleObject_Exit(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((*(uint32_t *)(arg1 + 0x20)) & (0xFFFFFF7FULL)) == 0) {
        a4 = *(uint64_t *)(arg1);
        a2 = Arg1 + 24;
        a3 = *(uint64_t *)(arg1 + 0x8);
        Arg1 = 1;
        result = ViDeadlockObjectAcquired(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA98E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA98E0[BB_00BA98E0]
  bb_00BA98ED[BB_00BA98ED]
  bb_00BA9902[BB_00BA9902]
  bb_00BA9907[BB_00BA9907]
  bb_00BA98E0 -->|branch| bb_00BA9902
  bb_00BA98E0 -->|fallthrough| bb_00BA98ED
  bb_00BA98ED -->|flow| bb_00BA9902
```
