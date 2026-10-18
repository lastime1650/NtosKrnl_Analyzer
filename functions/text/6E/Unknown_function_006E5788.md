# sub_006E5788

- RVA: `0x006E5788`–`0x006E57A6` (길이 `30` bytes)
- VA: `0x00000001406E5788`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008099C`
- 디코드: `7`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E578F` → [PspUnlockQuotaExpansion](../39/PspUnlockQuotaExpansion_function_00390E68.md) (function, `0x00390E68`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E57A1` → [PspExpandQuota + 0xA3](../39/PspExpandQuota_function_00390660.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E5788  8A 54 24 60                     mov dl, byte ptr [rsp + 0x60]
006E578C  48 8B CE                        mov rcx, rsi
006E578F  E8 D4 B6 CA FF                  call 0x140390e68
006E5794  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
006E579C  48 89 28                        mov qword ptr [rax], rbp
006E579F  32 C0                           xor al, al
006E57A1  E9 5D AF CA FF                  jmp 0x140390703
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E5788(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, unsigned __int8 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16)
{
    __int64 result;

    result = PspUnlockQuotaExpansion(v_rsi, a12, a3, a4);
    *(unsigned __int64 *)(a16) = v_rbp;
    result = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_006E5788(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint8_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, void *Arg16)
{
    uint8_t *arg16 = (uint8_t *)Arg16;

    int64_t result;

    result = PspUnlockQuotaExpansion(local_rsi, Arg12, Arg3, Arg4);
    *(uint64_t *)(arg16) = local_rbp;
    result = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg16` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E5788&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E5788[BB_006E5788]
```
