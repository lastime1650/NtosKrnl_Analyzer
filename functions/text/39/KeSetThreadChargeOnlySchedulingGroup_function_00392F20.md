# KeSetThreadChargeOnlySchedulingGroup

- RVA: `0x00392F20`–`0x00392F46` (길이 `38` bytes)
- VA: `0x0000000140392F20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00080D5C`
- 디코드: `9`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PspUpdateContainerImpersonation](PspUpdateContainerImpersonation_function_003931EC.md) at `0x0039333A`
- [PspUpdateContainerImpersonation](PspUpdateContainerImpersonation_function_003931EC.md) at `0x0039337F`
- [sub_00393F58](Unknown_function_00393F58.md) at `0x00393F5B`
- [sub_00393FA5](Unknown_function_00393FA5.md) at `0x00393FD4`
- [PspExitThread](../../page/90/PspExitThread_function_00905F60.md) at `0x009066DA`
- [sub_00B1B2E4](../../page/B1/Unknown_function_00B1B2E4.md) at `0x00B1B46E`
- [sub_00B1B2E4](../../page/B1/Unknown_function_00B1B2E4.md) at `0x00B1B4AA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00392F37` → [sub_00393013 + 0xC](Unknown_function_00393013.md) (`tail-transfer`)
  - `0x00392F40` → [sub_00393013 + 0x1D](Unknown_function_00393013.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00392F20  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
00392F25  57                              push rdi
00392F26  48 83 EC 20                     sub rsp, 0x20
00392F2A  F7 41 78 00 02 00 00            test dword ptr [rcx + 0x78], 0x200
00392F31  48 8B EA                        mov rbp, rdx
00392F34  48 8B F9                        mov rdi, rcx
00392F37  0F 84 E2 00 00 00               je 0x14039301f
00392F3D  48 85 D2                        test rdx, rdx
00392F40  0F 85 EA 00 00 00               jne 0x140393030
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KeSetThreadChargeOnlySchedulingGroup(__int64 a1, __int64 a2)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbp;
    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
void KeSetThreadChargeOnlySchedulingGroup(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbp;
    local_rsp = (local_rsp) - (32);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x78` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00392F20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00392F20[BB_00392F20]
  bb_00392F3D[BB_00392F3D]
  bb_00392F20 -->|fallthrough| bb_00392F3D
```
