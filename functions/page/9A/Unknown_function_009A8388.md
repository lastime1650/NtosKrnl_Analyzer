# sub_009A8388

- RVA: `0x009A8388`–`0x009A83B5` (길이 `45` bytes)
- VA: `0x00000001409A8388`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009CE68`
- 디코드: `12`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009A83A6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009A83A6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x009A839C` → [sub_009A831A + 0x18](Unknown_function_009A831A.md) (`tail-transfer`)
  - `0x009A83B0` → [IopFreeMiniCompletionPacket + 0x3A](IopFreeMiniCompletionPacket_function_009A82D0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009A8388  FF 47 20                        inc dword ptr [rdi + 0x20]
009A838B  48 8B B9 78 08 00 00            mov rdi, qword ptr [rcx + 0x878]
009A8392  FF 47 1C                        inc dword ptr [rdi + 0x1c]
009A8395  0F B7 47 10                     movzx eax, word ptr [rdi + 0x10]
009A8399  66 39 07                        cmp word ptr [rdi], ax
009A839C  72 94                           jb 0x1409a8332
009A839E  FF 47 20                        inc dword ptr [rdi + 0x20]
009A83A1  33 D2                           xor edx, edx
009A83A3  48 8B CB                        mov rcx, rbx
009A83A6  E8 C5 A4 1D 00                  call 0x140b82870
009A83AB  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
009A83B0  E9 55 FF FF FF                  jmp 0x1409a830a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009A8388(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;

    a2 = 0;
    result = ExFreePoolWithTag(v_rbx, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_009A8388(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    Arg2 = 0;
    result = ExFreePoolWithTag(local_rbx, Arg2, Arg3, Arg4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x878` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009A8388&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009A8388[BB_009A8388]
  bb_009A839E[BB_009A839E]
  bb_009A8388 -->|fallthrough| bb_009A839E
```
