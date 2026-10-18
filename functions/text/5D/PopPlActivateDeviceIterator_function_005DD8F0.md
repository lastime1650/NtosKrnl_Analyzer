# PopPlActivateDeviceIterator

- RVA: `0x005DD8F0`–`0x005DD92D` (길이 `61` bytes)
- VA: `0x00000001405DD8F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `19`개 명령, `61/61` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005DD908` → [PopPlLookupDevicePowerProfile](PopPlLookupDevicePowerProfile_function_005DDAD0.md) (function, `0x005DDAD0`)
- `0x005DD91F` → [PopFxActivateDevice](../4A/PopFxActivateDevice_function_004A0DC8.md) (function, `0x004A0DC8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005DD8F0  40 53                           push rbx
005DD8F2  48 83 EC 20                     sub rsp, 0x20
005DD8F6  48 8B 59 20                     mov rbx, qword ptr [rcx + 0x20]
005DD8FA  48 8B C2                        mov rax, rdx
005DD8FD  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
005DD901  48 8D 93 D8 00 00 00            lea rdx, [rbx + 0xd8]
005DD908  E8 C3 01 00 00                  call 0x1405ddad0
005DD90D  48 85 C0                        test rax, rax
005DD910  74 12                           je 0x1405dd924
005DD912  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
005DD916  45 33 C0                        xor r8d, r8d
005DD919  33 D2                           xor edx, edx
005DD91B  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
005DD91F  E8 A4 34 EC FF                  call 0x1404a0dc8
005DD924  B0 01                           mov al, 1
005DD926  48 83 C4 20                     add rsp, 0x20
005DD92A  5B                              pop rbx
005DD92B  C3                              ret
005DD92C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPlActivateDeviceIterator(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PopPlLookupDevicePowerProfile(*(unsigned __int64 *)(a2 + 8), *(unsigned __int64 *)(a1 + 32) + 216, a3, a4);
    if (result != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 48);
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(a1 + 32);
        result = PopFxActivateDevice(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t PopPlActivateDeviceIterator(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PopPlLookupDevicePowerProfile(*(uint64_t *)(arg2 + 0x8), *(uint64_t *)(arg1 + 0x20) + 216, Arg3, a4);
    if (result != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x30);
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x20);
        result = PopFxActivateDevice(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005DD8F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005DD8F0[BB_005DD8F0]
  bb_005DD912[BB_005DD912]
  bb_005DD924[BB_005DD924]
  bb_005DD92C[BB_005DD92C]
  bb_005DD8F0 -->|branch| bb_005DD924
  bb_005DD8F0 -->|fallthrough| bb_005DD912
  bb_005DD912 -->|flow| bb_005DD924
```
