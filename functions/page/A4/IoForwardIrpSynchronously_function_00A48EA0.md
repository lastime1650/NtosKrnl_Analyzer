# IoForwardIrpSynchronously

- RVA: `0x00A48EA0`–`0x00A48EED` (길이 `77` bytes)
- VA: `0x0000000140A48EA0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `22`개 명령, `77/77` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A48EDC` → [IoSynchronousCallDriver](../../text/48/IoSynchronousCallDriver_function_00484050.md) (function, `0x00484050`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A48EDC` → [IoSynchronousCallDriver](../../text/48/IoSynchronousCallDriver_function_00484050.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A48EA0  48 83 EC 28                     sub rsp, 0x28
00A48EA4  80 7A 43 01                     cmp byte ptr [rdx + 0x43], 1
00A48EA8  48 8B C1                        mov rax, rcx
00A48EAB  74 3C                           je 0x140a48ee9
00A48EAD  48 8B 8A B8 00 00 00            mov rcx, qword ptr [rdx + 0xb8]
00A48EB4  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00A48EB7  0F 11 41 B8                     movups xmmword ptr [rcx - 0x48], xmm0
00A48EBB  0F 10 49 10                     movups xmm1, xmmword ptr [rcx + 0x10]
00A48EBF  0F 11 49 C8                     movups xmmword ptr [rcx - 0x38], xmm1
00A48EC3  0F 10 41 20                     movups xmm0, xmmword ptr [rcx + 0x20]
00A48EC7  0F 11 41 D8                     movups xmmword ptr [rcx - 0x28], xmm0
00A48ECB  F2 0F 10 49 30                  movsd xmm1, qword ptr [rcx + 0x30]
00A48ED0  F2 0F 11 49 E8                  movsd qword ptr [rcx - 0x18], xmm1
00A48ED5  C6 41 BB 00                     mov byte ptr [rcx - 0x45], 0
00A48ED9  48 8B C8                        mov rcx, rax
00A48EDC  E8 6F B1 A3 FF                  call 0x140484050
00A48EE1  B0 01                           mov al, 1
00A48EE3  48 83 C4 28                     add rsp, 0x28
00A48EE7  C3                              ret
00A48EE8  CC                              int3
00A48EE9  32 C0                           xor al, al
00A48EEB  EB F6                           jmp 0x140a48ee3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoForwardIrpSynchronously(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(a2 + 67)) == 1) goto loc_00A48EE9;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) - 72) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) - 56) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) - 40) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) - 24) = v_xmm1;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 184) - 69) = 0;
    result = IoSynchronousCallDriver(a1, a2, a3, a4);
loc_00A48EE3:
    v_rsp = (v_rsp) + (40);
    return 1;
loc_00A48EE9:
    result = 0;
    goto loc_00A48EE3;
}
```

## 5. (Beta) C Style

```c
int64_t IoForwardIrpSynchronously(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(arg2 + 0x43)) == 1) goto loc_00A48EE9;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) - 0x48) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) - 0x38) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) - 0x28) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) - 0x18) = v_xmm1;
    *(uint8_t *)(*(uint64_t *)(arg2 + 0xB8) - 0x45) = 0;
    result = IoSynchronousCallDriver(Arg1, Arg2, a3, a4);
loc_00A48EE3:
    local_rsp = (local_rsp) + (40);
    return 1;
loc_00A48EE9:
    result = 0;
    goto loc_00A48EE3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x43` | `8` | `R` |
| `Arg2` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A48EA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A48EA0[BB_00A48EA0]
  bb_00A48EAD[BB_00A48EAD]
  bb_00A48EE3[BB_00A48EE3]
  bb_00A48EE8[BB_00A48EE8]
  bb_00A48EE9[BB_00A48EE9]
  bb_00A48EA0 -->|branch| bb_00A48EE9
  bb_00A48EA0 -->|fallthrough| bb_00A48EAD
  bb_00A48EAD -->|flow| bb_00A48EE3
  bb_00A48EE8 -->|flow| bb_00A48EE9
  bb_00A48EE9 -->|branch| bb_00A48EE3
```
