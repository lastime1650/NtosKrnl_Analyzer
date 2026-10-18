# KiSetDpcRequestFlag

- RVA: `0x0039DC50`–`0x0039DC7B` (길이 `43` bytes)
- VA: `0x000000014039DC50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00081B14`
- 디코드: `11`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00207D3E](../20/Unknown_function_00207D3E.md) at `0x00208222`
- [sub_00207D3E](../20/Unknown_function_00207D3E.md) at `0x002082A4`
- [KiUpdateRunTime](KiUpdateRunTime_function_0039BB70.md) at `0x0039C0C7`
- [sub_0039CA0B](Unknown_function_0039CA0B.md) at `0x0039CC30`
- [KiRequestTimer2Expiration](KiRequestTimer2Expiration_function_0039F118.md) at `0x0039F13F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0039DC75` → [sub_0039DD36](Unknown_function_0039DD36.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0039DC50  48 83 EC 08                     sub rsp, 8
0039DC54  44 0F B7 DA                     movzx r11d, dx
0039DC58  4C 8B D1                        mov r10, rcx
0039DC5B  45 33 C0                        xor r8d, r8d
0039DC5E  0F 0D 09                        prefetchw byte ptr [rcx]
0039DC61  0F B7 09                        movzx ecx, word ptr [rcx]
0039DC64  44 0F B7 C9                     movzx r9d, cx
0039DC68  0F B7 C1                        movzx eax, cx
0039DC6B  66 44 0B CA                     or r9w, dx
0039DC6F  66 F0 45 0F B1 0A               lock cmpxchg word ptr [r10], r9w
0039DC75  0F 84 BB 00 00 00               je 0x14039dd36
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiSetDpcRequestFlag(__int64 a1, unsigned __int16 a2, int a3)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (8);
    a3 = 0;
    a4 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a1))) | (a2));
}
```

## 5. (Beta) C Style

```c
int64_t KiSetDpcRequestFlag(void *Arg1, uint16_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (8);
    Arg3 = 0;
    a4 = (uint16_t)(((uint16_t)(*(uint16_t *)(arg1))) | (Arg2));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0039DC50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0039DC50[BB_0039DC50]
```
