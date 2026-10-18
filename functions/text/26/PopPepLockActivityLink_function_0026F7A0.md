# PopPepLockActivityLink

- RVA: `0x0026F7A0`–`0x0026F7CA` (길이 `42` bytes)
- VA: `0x000000014026F7A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000658A0`
- 디코드: `12`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopPepSurprisePowerOn](PopPepSurprisePowerOn_function_0026E480.md) at `0x0026E4AA`
- [PopPepUpdateConstraints](PopPepUpdateConstraints_function_0026F5C8.md) at `0x0026F5FE`
- [PopPepCompleteComponentIdleState](../4D/PopPepCompleteComponentIdleState_function_004D8EC4.md) at `0x004D8F08`
- [PopPepComponentSetResidency](../5D/PopPepComponentSetResidency_function_005DC9A4.md) at `0x005DCA02`
- [PopPepComponentSetWakeHint](../5D/PopPepComponentSetWakeHint_function_005DCAA0.md) at `0x005DCAFC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0026F7BB` → [sub_0026F7CA](Unknown_function_0026F7CA.md) (`tail-transfer`)
  - `0x0026F7C4` → [sub_0026F86B + 0x1](Unknown_function_0026F86B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0026F7A0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0026F7A5  56                              push rsi
0026F7A6  57                              push rdi
0026F7A7  41 56                           push r14
0026F7A9  48 83 EC 20                     sub rsp, 0x20
0026F7AD  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
0026F7B2  48 8B DA                        mov rbx, rdx
0026F7B5  48 8B F9                        mov rdi, rcx
0026F7B8  48 85 D2                        test rdx, rdx
0026F7BB  74 0D                           je 0x14026f7ca
0026F7BD  83 B9 B4 00 00 00 01            cmp dword ptr [rcx + 0xb4], 1
0026F7C4  0F 85 A2 00 00 00               jne 0x14026f86c
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall PopPepLockActivityLink(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (32);
}
```

## 5. (Beta) C Style

```c
void PopPepLockActivityLink(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (32);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0026F7A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0026F7A0[BB_0026F7A0]
  bb_0026F7BD[BB_0026F7BD]
  bb_0026F7A0 -->|fallthrough| bb_0026F7BD
```
