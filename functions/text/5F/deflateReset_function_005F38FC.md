# deflateReset

- RVA: `0x005F38FC`–`0x005F392B` (길이 `47` bytes)
- VA: `0x00000001405F38FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `16`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005F3909` → [deflateResetKeep](deflateResetKeep_function_005F3934.md) (function, `0x005F3934`)
- `0x005F3918` → [lm_init](lm_init_function_005F52D4.md) (function, `0x005F52D4`)

### Direct callers
- [RtlCompressDeflateInitCompressionStream](RtlCompressDeflateInitCompressionStream_function_005F1F74.md) at `0x005F20C9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005F38FC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005F3901  57                              push rdi
005F3902  48 83 EC 20                     sub rsp, 0x20
005F3906  48 8B F9                        mov rdi, rcx
005F3909  E8 26 00 00 00                  call 0x1405f3934
005F390E  8B D8                           mov ebx, eax
005F3910  85 C0                           test eax, eax
005F3912  75 09                           jne 0x1405f391d
005F3914  48 8B 4F 28                     mov rcx, qword ptr [rdi + 0x28]
005F3918  E8 B7 19 00 00                  call 0x1405f52d4
005F391D  8B C3                           mov eax, ebx
005F391F  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005F3924  48 83 C4 20                     add rsp, 0x20
005F3928  5F                              pop rdi
005F3929  C3                              ret
005F392A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall deflateReset(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = deflateResetKeep(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) {
        a1 = *(unsigned __int64 *)(a1 + 40);
        result = lm_init(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t deflateReset(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = deflateResetKeep(Arg1, a2, a3, a4);
    if ((uint32_t)(result) == 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x28);
        result = lm_init(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005F38FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005F38FC[BB_005F38FC]
  bb_005F3914[BB_005F3914]
  bb_005F391D[BB_005F391D]
  bb_005F392A[BB_005F392A]
  bb_005F38FC -->|branch| bb_005F391D
  bb_005F38FC -->|fallthrough| bb_005F3914
  bb_005F3914 -->|flow| bb_005F391D
```
