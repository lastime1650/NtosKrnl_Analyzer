# sub_006E61FC

- RVA: `0x006E61FC`–`0x006E622B` (길이 `47` bytes)
- VA: `0x00000001406E61FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00081CB8`
- 디코드: `13`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E61FC` → [KiDisconnectSecondaryInterruptInternal](../4B/KiDisconnectSecondaryInterruptInternal_function_004BCBD4.md) (function, `0x004BCBD4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E6226` → [KiProcessPendingDisconnect + 0x1C](../39/KiProcessPendingDisconnect_function_0039F374.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E61FC  E8 D3 69 DD FF                  call 0x1404bcbd4
006E6201  89 46 10                        mov dword ptr [rsi + 0x10], eax
006E6204  48 83 C3 08                     add rbx, 8
006E6208  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
006E620C  48 39 38                        cmp qword ptr [rax], rdi
006E620F  74 07                           je 0x1406e6218
006E6211  B9 03 00 00 00                  mov ecx, 3
006E6216  CD 29                           int 0x29
006E6218  48 89 3B                        mov qword ptr [rbx], rdi
006E621B  48 89 43 08                     mov qword ptr [rbx + 8], rax
006E621F  48 89 18                        mov qword ptr [rax], rbx
006E6222  48 89 5F 08                     mov qword ptr [rdi + 8], rbx
006E6226  E9 65 91 CB FF                  jmp 0x14039f390
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E61FC(void)
{
    __int64 result;
    __int64 v_rbx;

    result = KiDisconnectSecondaryInterruptInternal(a1, a2, a3, a4);
    *(unsigned int *)(v_rsi + 16) = (unsigned int)(result);
    v_rbx = (v_rbx) + (8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8))) != v_rdi) {
        a1 = 3;
    }
    *(unsigned __int64 *)(v_rbx) = v_rdi;
    *(unsigned __int64 *)(v_rbx + 8) = *(unsigned __int64 *)(v_rdi + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8)) = v_rbx;
    *(unsigned __int64 *)(v_rdi + 8) = v_rbx;
}
```

## 5. (Beta) C Style

```c
void sub_006E61FC(void)
{
    int64_t result;
    int64_t local_rbx;

    result = KiDisconnectSecondaryInterruptInternal(a1, a2, a3, a4);
    *(uint32_t *)(local_rsi + 0x10) = (uint32_t)(result);
    local_rbx = (local_rbx) + (8);
    if ((*(uint64_t *)(*(uint64_t *)(local_rdi + 0x8))) != local_rdi) {
        a1 = 3;
    }
    *(uint64_t *)(local_rbx) = local_rdi;
    *(uint64_t *)(local_rbx + 0x8) = *(uint64_t *)(local_rdi + 0x8);
    *(uint64_t *)(*(uint64_t *)(local_rdi + 0x8)) = local_rbx;
    *(uint64_t *)(local_rdi + 0x8) = local_rbx;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E61FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E61FC[BB_006E61FC]
  bb_006E6211[BB_006E6211]
  bb_006E6218[BB_006E6218]
  bb_006E61FC -->|branch| bb_006E6218
  bb_006E61FC -->|fallthrough| bb_006E6211
  bb_006E6211 -->|flow| bb_006E6218
```
