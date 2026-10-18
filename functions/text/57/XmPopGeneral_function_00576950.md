# XmPopGeneral

- RVA: `0x00576950`–`0x00576996` (길이 `70` bytes)
- VA: `0x0000000140576950`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `22`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00576975` → [XmEvaluateAddressSpecifier](../47/XmEvaluateAddressSpecifier_function_00473224.md) (function, `0x00473224`)
- `0x00576985` → [XmSetDestinationValue](../47/XmSetDestinationValue_function_004734EC.md) (function, `0x004734EC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00576950  40 53                           push rbx
00576952  48 83 EC 20                     sub rsp, 0x20
00576956  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
0057695B  48 8B D9                        mov rbx, rcx
0057695E  8A 81 8A 00 00 00               mov al, byte ptr [rcx + 0x8a]
00576964  F6 D8                           neg al
00576966  1B D2                           sbb edx, edx
00576968  83 E2 02                        and edx, 2
0057696B  FF C2                           inc edx
0057696D  89 51 78                        mov dword ptr [rcx + 0x78], edx
00576970  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00576975  E8 AA C8 EF FF                  call 0x140473224
0057697A  48 85 C0                        test rax, rax
0057697D  74 10                           je 0x14057698f
0057697F  48 8B D0                        mov rdx, rax
00576982  48 8B CB                        mov rcx, rbx
00576985  E8 62 CB EF FF                  call 0x1404734ec
0057698A  B8 01 00 00 00                  mov eax, 1
0057698F  48 83 C4 20                     add rsp, 0x20
00576993  5B                              pop rbx
00576994  C3                              ret
00576995  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall XmPopGeneral(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (32);
    result = (unsigned __int8)(-(*(unsigned __int8 *)(a1 + 138)));
    a2 = (unsigned int)((a2) & (2));
    a2 = (unsigned int)((a2) + 1);
    *(unsigned int *)(a1 + 120) = a2;
    result = XmEvaluateAddressSpecifier(a1, v_stack_p8, a3, a4);
    if (result != 0) {
        a2 = result;
        a1 = a1;
        result = XmSetDestinationValue(a1, a2, a3, a4);
        result = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t XmPopGeneral(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (32);
    result = (uint8_t)(-(*(uint8_t *)(arg1 + 0x8A)));
    Arg2 = (uint32_t)((Arg2) & (2));
    Arg2 = (uint32_t)((Arg2) + 1);
    *(uint32_t *)(arg1 + 0x78) = Arg2;
    result = XmEvaluateAddressSpecifier(Arg1, v_stack_p8, a3, a4);
    if (result != 0) {
        Arg2 = result;
        Arg1 = Arg1;
        result = XmSetDestinationValue(Arg1, Arg2, a3, a4);
        result = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x78` | `32` | `W` |
| `Arg1` | `+ 0x8A` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00576950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00576950[BB_00576950]
  bb_0057697F[BB_0057697F]
  bb_0057698F[BB_0057698F]
  bb_00576995[BB_00576995]
  bb_00576950 -->|branch| bb_0057698F
  bb_00576950 -->|fallthrough| bb_0057697F
  bb_0057697F -->|flow| bb_0057698F
```
